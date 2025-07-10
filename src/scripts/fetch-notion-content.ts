import path from "path"
import { NotionClient } from "./notion-client"
import dotenv from 'dotenv'
import fs from 'fs'
import { Cours, Danse } from "~/models"
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);


dotenv.config()

const notionClient = new NotionClient(process.env.NOTION_API_KEY!, process.env.NOTION_DANSES_DATABASE_ID!, process.env.NOTION_COURS_DATABASE_ID!)

const notionCacheOutputDir = path.resolve(__dirname, '../public/notion-cache')

async function saveToNotionCache(items: any[], collectionName: string) {
  const outputDir = path.join(notionCacheOutputDir, collectionName)

  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true })
  }

  const itemsFilePath = path.join(outputDir, `${collectionName}.json`)
  fs.writeFileSync(itemsFilePath, JSON.stringify(items, null, 2), 'utf-8')
  console.log(`✅ Saved: ${itemsFilePath}`)
}

async function main() {
  try {
    const dansePages = await notionClient.fetchDansePages()
    const coursPages = await notionClient.fetchCoursPages()
    const danses = dansePages.map(dansePage => Danse.fromNotion(dansePage))
    const cours = coursPages.map(coursPage => Cours.fromNotion(coursPage, danses))
    await saveToNotionCache(danses, "danses")
    await saveToNotionCache(cours, "cours")
    console.log('✅ All Notion databases saved.')
  } catch (err) {
    console.error('❌ Failed:', err)
  }
}

main()