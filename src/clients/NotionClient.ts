import { Client } from '@notionhq/client'

export class NotionClient {
  private client: Client
  private databaseIds: {
    danses: string
    cours: string
  }

  constructor() {
    const config = useRuntimeConfig()
    this.client = new Client({ auth: config.NOTION_API_KEY })
    this.databaseIds = {
      danses: config.NOTION_DANSES_DATABASE_ID,
      cours: config.NOTION_COURS_DATABASE_ID,
    }
  }

  async fetchDanses() {
    const res = await this.client.databases.query({
      database_id: this.databaseIds.danses,
    })
    return res.results
  }

  async fetchCours() {
    const res = await this.client.databases.query({
      database_id: this.databaseIds.cours,
    })
    return res.results
  }
}
