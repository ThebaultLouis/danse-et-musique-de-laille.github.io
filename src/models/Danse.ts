export class Danse {
  constructor(
    public id: string,
    public nom: string,
    public musiqueUrl: string,
    public videoUrl: string,
    public pdfUrl: string
  ) { }

  static fromNotion(page: any): Danse {
    const id = page.id
    const nom = page.properties?.Nom?.title?.[0]?.plain_text || ''
    const musiqueUrl = page.properties?.['Lien de la musique']?.url || ''
    const videoUrl = page.properties?.['Lien de la chorégraphie']?.url || ''
    const pdfUrl = page.properties?.['Pdf de la chorégraphie']?.files?.[0]?.file?.url || ''
    return new Danse(
      id,
      nom,
      musiqueUrl,
      videoUrl,
      pdfUrl
    )
  }
}
