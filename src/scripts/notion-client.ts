import { Client, collectPaginatedAPI } from '@notionhq/client'

export class NotionClient {
  private client: Client
  private databaseIds: {
    danses: string
    cours: string
  }

  constructor(api_key: string, danses_database_id: string, cours_dabases_id: string) {
    this.client = new Client({ auth: api_key })
    this.databaseIds = {
      danses: danses_database_id,
      cours: cours_dabases_id,
    }
  }

  async fetchDanseDatabaseProperties() {
    return this.client.databases.retrieve({ database_id: this.databaseIds.danses })
  }

  async fetchDansePages() {
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

  async fetchCoursDatabaseProperties() {
    return this.client.databases.retrieve({ database_id: this.databaseIds.cours })
  }

  async fetchCoursPages() {
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
