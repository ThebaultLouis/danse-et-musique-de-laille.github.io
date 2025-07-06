import { defineStore } from 'pinia'
import { NotionClient } from '~/clients/NotionClient'
import { Cours, type TCours } from '~/models/Cours'
import { Danse, type TDanse } from '~/models/Danse'

export const useNotionDanseStore = defineStore('notionDanse', {
  state: () => ({
    danses: [] as TDanse[],
    loaded: false,
  }),

  actions: {
    async fetchDanses() {
      if (this.loaded) return
      const results = await new NotionClient().fetchDanses()
      this.danses = results.map(Danse.toPinia)
      this.loaded = true
    },
  },
})

export const useNotionCoursStore = defineStore('notionCours', {
  state: () => ({
    cours: [] as TCours[],
    loaded: false,
  }),

  actions: {
    async fetchCours() {
      if (this.loaded) return
      const results = await new NotionClient().fetchCours()
      this.cours = results.map(Cours.toPinia)
      this.loaded = true
    },
  },
})

