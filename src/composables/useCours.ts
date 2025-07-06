import { computed } from 'vue'
import { Cours } from '~/models/Cours'

export function useCours() {
  const store = useNotionCoursStore()

  const cours = computed(() =>
    store.cours.map((obj) => Cours.fromPinia(obj))
  )

  return { cours, fetchCours: store.fetchCours }
}