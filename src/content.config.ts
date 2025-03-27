import { defineCollection, defineContentConfig, z } from '@nuxt/content'
import { CourSchema, DanseSchema } from './content/schemas'

export default defineContentConfig({
  collections: {
    cours: defineCollection({
      type: 'data',
      source: 'cours/**.yml',
      schema: CourSchema
    }),
    danses: defineCollection({
      type: 'page',
      source: 'danses/**.yml',
      schema: DanseSchema
    }),
  }
})

