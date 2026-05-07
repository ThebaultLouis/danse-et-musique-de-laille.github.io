import { Client, collectPaginatedAPI } from '@notionhq/client'
import { Config } from './config'
import { s3UrlToCloudFrontUrl, isS3Url } from './cloudfront'

const notionClient = new Client({ auth: Config.NOTION_API_KEY })

const PDF_PROPERTY = 'Pdf de la chorégraphie'

async function migrateDanses() {
  const pages = await collectPaginatedAPI(notionClient.databases.query, {
    database_id: Config.NOTION_DANSES_DATABASE_ID,
  })

  let updated = 0
  let skipped = 0

  for (const page of pages) {
    const fileProperty = (page as any).properties[PDF_PROPERTY]
    if (!fileProperty || fileProperty.type !== 'files' || fileProperty.files.length === 0) {
      skipped++
      continue
    }

    const file = fileProperty.files[0]
    if (file.type !== 'external') {
      skipped++
      continue
    }

    const currentUrl: string = file.external.url
    if (!isS3Url(currentUrl)) {
      skipped++
      continue
    }

    const cloudfrontUrl = s3UrlToCloudFrontUrl(currentUrl)

    await notionClient.pages.update({
      page_id: page.id,
      properties: {
        [PDF_PROPERTY]: {
          files: [{ name: file.name, external: { url: cloudfrontUrl } }],
        },
      },
    })

    const nom = (page as any).properties?.Nom?.title?.[0]?.plain_text || page.id
    console.log(`✅ ${nom}: ${currentUrl} → ${cloudfrontUrl}`)
    updated++
  }

  console.log(`\nDone. Updated: ${updated}, Skipped: ${skipped}`)
}

async function main() {
  try {
    await migrateDanses()
  } catch (err) {
    console.error('❌ Migration failed:', err)
    process.exit(1)
  }
}

main()
