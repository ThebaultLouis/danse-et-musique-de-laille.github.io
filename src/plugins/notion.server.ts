export default defineNuxtPlugin(async () => {
  const danseStore = useNotionDanseStore()
  await danseStore.fetchDanses()

  const coursStore = useNotionCoursStore()
  await coursStore.fetchCours()
})
