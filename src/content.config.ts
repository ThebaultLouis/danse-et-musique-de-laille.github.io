import { defineCollection, defineContentConfig, z } from '@nuxt/content'

const CourSchema = z.object({
  type: z.enum(['COUNTRY']),
  niveau: z.enum(['BEGINNER', 'INTERMEDIATE', 'ADVANCED']),
  danses_revisees: z.array(z.string()),
  danse_apprise: z.array(z.string()),
  date_realisation: z.date()
});

const DanseSchema = z.object({
  nom: z.string().min(1, { message: "Le nom de la danse est requis" }),
  lien_musique: z.string().url().nullable(),
  video_choregraphie: z.string().url().optional(),
  pdf_choregraphie: z.string().url().optional(),
});

export default defineContentConfig({
  collections: {
    cours: defineCollection({
      type: 'data',
      source: 'cours/**.yml',
      schema: CourSchema
    }),
    danses: defineCollection({
      type: 'data',
      source: 'danses/**.yml',
      schema: DanseSchema
    }),
  }
})

