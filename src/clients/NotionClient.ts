import { Client, collectPaginatedAPI } from '@notionhq/client'

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
    const danses = await collectPaginatedAPI(this.client.databases.query, {
      database_id: this.databaseIds.danses,
      sorts: [
        {
          property: "Nom",
          direction: "ascending",
        },
      ],
    })
    return danses
  }

  async fetchCours() {
    const cours = await collectPaginatedAPI(this.client.databases.query, {
      database_id: this.databaseIds.cours,
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
    return cours
  }
}
