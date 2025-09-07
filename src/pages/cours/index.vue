<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Historique des Cours
    </h1>
    <div v-if="cours">
      <div class="mb-8 flex justify-center space-x-4">
        <select
          v-model="selectedNiveau"
          class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
        >
          <option value="">Tous les niveaux</option>
          <option v-for="niveau in niveaux" :key="niveau" :value="niveau">
            {{ niveau }}
          </option>
        </select>

        <select
          v-model="selectedType"
          class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
        >
          <option value="">Tous les types</option>
          <option
            v-for="typeDeDanses in typesDeDanses"
            :key="typeDeDanses"
            :value="typeDeDanses"
          >
            {{ typeDeDanses }}
          </option>
        </select>

        <select
          v-model="selectedDate"
          class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
        >
          <option value="">Tous les jours</option>
          <option v-for="date in joursDeDanses" :key="date" :value="date">
            {{ date }}
          </option>
        </select>
      </div>

      <div class="overflow-x-auto">
        <table
          v-if="cours"
          class="w-full bg-white shadow-md rounded-lg overflow-hidden"
        >
          <thead class="bg-gray-100">
            <tr>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/10"
              >
                Date
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/10"
              >
                Type
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/10"
              >
                Niveau
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/5"
              >
                Danses Apprises
              </th>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-1/2"
              >
                Danses Révisées
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="cours in filteredCours"
              :key="cours.id"
              class="hover:bg-gray-50 transition-colors"
            >
              <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ cours.date }}
              </td>
              <td class="px-4 py-4 whitespace-nowrap">
                <span class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
                  {{ cours.type }}
                </span>
              </td>
              <td class="px-4 py-4 whitespace-nowrap">
                <span
                  :class="`bg-${typeDeDanseParCouleur[cours.niveau]}-100 text-${
                    typeDeDanseParCouleur[cours.niveau]
                  }-800`"
                  class="px-2 py-1 rounded-full text-xs font-medium"
                >
                  {{ cours.niveau }}
                </span>
              </td>
              <td class="px-4 py-4">
                <ul class="space-y-1">
                  <li
                    v-for="danse in cours.dansesApprises"
                    :key="danse.id"
                    class="text-gray-700"
                  >
                    <NuxtLink
                      :to="`danses/${danse.id}`"
                      class="hover:text-blue-600 hover:underline"
                    >
                      {{ danse.nom }}
                    </NuxtLink>
                  </li>
                </ul>
              </td>
              <td class="px-4 py-4 text-gray-700">
                <span
                  v-for="(danse, index) in cours.dansesRevisees"
                  :key="danse.id"
                >
                  <NuxtLink
                    :to="`danses/${danse.id}`"
                    class="hover:text-blue-600 hover:underline"
                  >
                    {{ danse.nom }}
                  </NuxtLink>
                  <span v-if="index < cours.dansesRevisees.length - 1">, </span>
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: "Cours de danse - DML Country",
  meta: [
    {
      name: "description",
      content:
        "Découvrez tous nos cours de danse Country à Laillé (35) pour tous niveaux.",
    },
    { property: "og:title", content: "Cours de danse - DML Country" },
    {
      property: "og:description",
      content:
        "Découvrez tous nos cours de danse country à Laillé (35) pour tous niveaux.",
    },
    { property: "og:type", content: "website" },
    { property: "og:url", content: "https://dml-country/cours" },
  ],
});

const { data: cours } = await useFetch<Cours[]>(`/cache/cours.json`);
const { data: coursDatabaseProperties } = await useFetch(
  `/cache/cours-database-properties.json`
);
const route = useRoute();
const router = useRouter();

const niveaux = computed(
  () => new Set(cours.value?.map((cours: Cours) => cours.niveau))
);
const typesDeDanses = computed(
  () => new Set(cours.value?.map((cours: Cours) => cours.type))
);
const joursDeDanses = computed(
  () => new Set(cours.value?.map((cours: Cours) => cours.date))
);
const typeDeDanseParCouleur = computed(() =>
  Object.fromEntries(
    coursDatabaseProperties.value?.properties?.Niveau?.select?.options.map(
      (option) => [option.name, option.color]
    ) || []
  )
);

const selectedNiveau = ref(route.query.niveau || "");
const selectedType = ref(route.query.type || "");
const selectedDate = ref(route.query.date || "");

watch([selectedNiveau, selectedType, selectedDate], ([niveau, type, date]) => {
  console.log(type);
  router.replace({
    query: {
      ...route.query,
      niveau: niveau || undefined,
      type: type || undefined,
      date: date || undefined,
    },
  });
});

const filteredCours = computed(() => {
  if (!cours.value) {
    return [];
  }
  return cours.value.filter((c) => {
    const matchNiveau =
      !selectedNiveau.value || c.niveau === selectedNiveau.value;
    const matchType = !selectedType.value || c.type === selectedType.value;
    const matchDate = !selectedDate.value || c.date === selectedDate.value;

    return matchNiveau && matchType && matchDate;
  });
});
</script>