import { NotionClient } from "./notion-client"
import dotenv from 'dotenv'
import { Cours, Danse } from "~/models"
import { saveObjectLocally } from "./save-object-locally"

dotenv.config()

const notionClient = new NotionClient(process.env.NOTION_API_KEY!, process.env.NOTION_DANSES_DATABASE_ID!, process.env.NOTION_COURS_DATABASE_ID!)


async function main() {
  try {
    const dansePages = await notionClient.fetchDansePages()
    const coursPages = await notionClient.fetchCoursPages()
    const danses = dansePages.map(dansePage => Danse.fromNotion(dansePage))
    const cours = coursPages.map(coursPage => Cours.fromNotion(coursPage, danses))
    saveObjectLocally(danses, "danses.json")
    saveObjectLocally(cours, "cours.json")
    console.log('✅ All Notion databases saved.')
  } catch (err) {
    console.error('❌ Failed:', err)
  }
}

main()