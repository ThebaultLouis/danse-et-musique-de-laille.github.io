export type TDanse = {
  id: string
  nom: string
  musiqueUrl: string
  videoUrl: string
  pdfUrl: string
}

export class Danse {
  constructor(
    public id: string,
    public nom: string,
    public musiqueUrl: string,
    public videoUrl: string,
    public pdfUrl: string
  ) { }

  get nuxtPath() {
    return `danses/${this.id}`
  }

  static toPinia(page: any): TDanse {
    return {
      id: page.id,
      nom: page.properties?.Nom?.title?.[0]?.plain_text || '',
      musiqueUrl: page.properties?.['Lien de la musique']?.url || '',
      videoUrl: page.properties?.['Lien de la chorégraphie']?.url || '',
      pdfUrl: page.properties?.['Pdf de la chorégraphie']?.files?.[0]?.file?.url || ''
    }
  }

  static fromPinia(danse: TDanse) {
    return new Danse(danse.id, danse.nom, danse.musiqueUrl, danse.videoUrl, danse.pdfUrl)
  }
}
