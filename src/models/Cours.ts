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
    public apprises: string[],
    public revisees: string[]
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

  static fromPinia(cours: TCours) {
    return new Cours(cours.id, cours.type, cours.date, cours.niveau, cours.dansesApprises, cours.dansesRevisees)
  }
}
