import { NotionClient } from "./notion-client"
import dotenv from 'dotenv'
import { Cours, Danse } from "~/models"
import { saveObjectLocally } from "./save-object-locally"

dotenv.config()

const notionClient = new NotionClient(
  process.env.NOTION_API_KEY!,
  process.env.NOTION_DANSES_DATABASE_ID!,
  process.env.NOTION_COURS_DATABASE_ID!
)

async function cacheDanseDatabase() {
  const danseDatabaseProperties = await notionClient.fetchDanseDatabaseProperties()
  const dansePages = await notionClient.fetchDansePages()
  const danses = dansePages.map(dansePage => Danse.fromNotion(dansePage))
  saveObjectLocally(danseDatabaseProperties, "danse-database-properties.json")
  saveObjectLocally(danses, "danses.json")
  return danses
}

async function cacheCoursDatabase(danses: Danse[]) {
  const coursDatabaseProperties = await notionClient.fetchCoursDatabaseProperties()
  const coursPages = await notionClient.fetchCoursPages()
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