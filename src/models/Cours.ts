import type { Danse } from "./Danse"

export type TCours = {
  id: string
  type: string
  date: string
  niveau: string
  dansesApprises: string[]
  dansesRevisees: string[]
}

export class Cours {
  constructor(
    public id: string,
    public type: string,
    public date: string,
    public niveau: string,
    public dansesApprises: Danse[],
    public dansesRevisees: Danse[]
  ) { }

  static toPinia(page: any): TCours {
    return {
      id: page.id,
      date: page.properties?.Date?.title?.[0]?.plain_text || '',
      type: page.properties?.Type?.select?.name || '',
      niveau: page.properties?.Niveau?.select?.name || '',
      dansesApprises: (page.properties?.['Danses apprises']?.relation || []).map((r: any) => r.id),
      dansesRevisees: (page.properties?.['Danses révisées']?.relation || []).map((r: any) => r.id)
    }
  }

  static fromPinia(cours: TCours, danses: Danse[]) {
    const danse_id_to_danse = Object.fromEntries(danses.map(danse => [danse.id, danse]))
    const dansesApprises = cours.dansesApprises.map(d => danse_id_to_danse[d])
    const dansesRevisees = cours.dansesRevisees.map(d => danse_id_to_danse[d])
    return new Cours(cours.id, cours.type, cours.date, cours.niveau, dansesApprises, dansesRevisees)
  }
}
