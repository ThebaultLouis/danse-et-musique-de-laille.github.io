import { defineCollection, defineContentConfig, z } from '@nuxt/content'
import { CourSchema, DanseSchema } from './content/schemas'

export default defineContentConfig({
  collections: {
    cours: defineCollection({
      type: 'data',
      source: 'cours/**.yaml',
      schema: CourSchema
    }),
    danses: defineCollection({
      type: 'data',
      source: 'danses/**.yaml',
      schema: DanseSchema
    }),
  }
})

