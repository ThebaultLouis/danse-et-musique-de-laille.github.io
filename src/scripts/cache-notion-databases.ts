import { Cours, Danse } from "~/models"
import { saveObjectLocally } from "./save-object-locally"
import { Client, collectPaginatedAPI } from '@notionhq/client'
import { Config } from './config'


const notionClient = new Client({ auth: Config.NOTION_API_KEY! })


async function cacheDanseDatabase() {
  const danseDatabaseId = Config.NOTION_DANSES_DATABASE_ID!
  const danseDatabaseProperties = await notionClient.databases.retrieve({ database_id: danseDatabaseId })
  const dansePages = await collectPaginatedAPI(notionClient.databases.query, {
    database_id: danseDatabaseId,
    sorts: [
      {
        property: "Nom",
        direction: "ascending",
      },
    ],
  })
  const danses = dansePages.map(dansePage => Danse.fromNotion(dansePage))
  saveObjectLocally(danseDatabaseProperties, "danse-database-properties.json")
  saveObjectLocally(danses, "danses.json")
  return danses
}

async function cacheCoursDatabase(danses: Danse[]) {
  const coursDatabaseId = Config.NOTION_COURS_DATABASE_ID!
  const coursDatabaseProperties = await notionClient.databases.retrieve({ database_id: coursDatabaseId })
  const coursPages = await collectPaginatedAPI(notionClient.databases.query, {
    database_id: coursDatabaseId,
    sorts: [
      {
        property: "Date",
        direction: "descending",
      },
      {
        property: "Niveau",
        direction: "descending",
      },
    ],
  })
  const cours = coursPages.map(coursPage => Cours.fromNotion(coursPage, danses))
  saveObjectLocally(coursDatabaseProperties, "cours-database-properties.json")
  saveObjectLocally(cours, "cours.json")
  return cours
}

async function main() {
  try {
    const danses = await cacheDanseDatabase()
    await cacheCoursDatabase(danses)
    console.log('✅ All Notion databases saved.')
  } catch (err) {
    console.error('❌ Failed:', err)
  }
}

main()