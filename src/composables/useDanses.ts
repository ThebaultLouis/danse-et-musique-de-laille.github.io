import { computed } from 'vue'
import { Danse } from '@/models/Danse'

export function useDanses() {
  const store = useNotionDanseStore()

  // Automatically convert plain objects to Danse class instances
  const danses = computed(() =>
    store.danses.map((obj) => Danse.fromPinia(obj))
  )

  return { danses, fetchDanses: store.fetchDanses }
}