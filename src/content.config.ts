import { defineCollection, defineContentConfig, z } from '@nuxt/content'
import { CoursSchema, DanseSchema } from './content/schemas'

export default defineContentConfig({
  collections: {
    cours: defineCollection({
      type: 'data',
      source: 'cours/**.yml',
      schema: CoursSchema
    }),
    danses: defineCollection({
      type: 'page',
      source: 'danses/**.yml',
      schema: DanseSchema
    }),
    pages: defineCollection({
      type: 'page',
      source: 'pages/**.md',
      schema: z.object({})
    })
  }
})

