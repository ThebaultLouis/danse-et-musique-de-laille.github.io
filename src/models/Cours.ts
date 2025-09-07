import type { Danse } from "./Danse"

export class Cours {
  constructor(
    public id: string,
    public type: string,
    public date: string,
    public niveau: string,
    public dansesApprises: Danse[],
    public dansesRevisees: Danse[]
  ) { }

  static fromNotion(page: any, danses: Danse[]): Cours {
    const id = page.id
    const date = page.properties?.Date?.title?.[0]?.plain_text || ''
    const type = page.properties?.Type?.select?.name || ''
    const niveau = page.properties?.Niveau?.select?.name || ''


    const notionDansesApprisesIds: string[] = (page.properties?.['Danses apprises']?.relation || []).map((r: any) => r.id)
    const notionDansesReviseesIds: string[] = (page.properties?.['Danses révisées']?.relation || []).map((r: any) => r.id)
    const danse_id_to_danse = Object.fromEntries(danses.map(danse => [danse.id, danse]))
    const dansesApprises = notionDansesApprisesIds.map(d => danse_id_to_danse[d])
    const dansesRevisees = notionDansesReviseesIds.map(d => danse_id_to_danse[d])

    return new Cours(
      id,
      type,
      date,
      niveau,
      dansesApprises,
      dansesRevisees
    )
  }
}
