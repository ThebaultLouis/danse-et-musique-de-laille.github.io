import { computed } from 'vue'
import { Cours } from '~/models/Cours'

export function useCours() {
  const notionCoursStore = useNotionCoursStore()
  const { danses } = useDanses()

  const cours = computed(() =>
    notionCoursStore.cours.map((obj) => Cours.fromPinia(obj, danses.value))
  )

  return { cours, fetchCours: notionCoursStore.fetchCours }
}