import { NotionClient } from "./notion-client"
import dotenv from 'dotenv'
import { saveObjectLocally } from "./save-object-locally"

dotenv.config()

const notionClient = new NotionClient(process.env.NOTION_API_KEY!, process.env.NOTION_DANSES_DATABASE_ID!, process.env.NOTION_COURS_DATABASE_ID!)


async function main() {

  // const dansePages = await notionClient.fetchDansePages()
  // saveObjectLocally(dansePages, "test.json")
  const properties = await notionClient.fetchDanseDatabaseProperties()
  console.log(properties)
  console.log(properties.properties["Niveau"]["select"]["options"][0])
  // saveObjectLocally(properties, "test.json")


}

main()