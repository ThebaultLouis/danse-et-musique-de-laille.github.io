<template>
  <div v-if="danse" class="flex justify-center py-12 px-4">
    <div class="w-full max-w-2xl text-center">
      <!-- Title -->
      <h1 class="text-4xl font-bold text-gray-800 mb-8">
        {{ danse.nom }}
      </h1>

      <!-- Sections -->
      <div class="space-y-10">
        <!-- Musique -->
        <section>
          <h2 class="text-2xl font-semibold mb-4">Musique</h2>
          <div class="space-y-4">
            <a
              v-if="danse?.musiqueUrl"
              :href="danse.musiqueUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="block bg-gray-100 rounded-xl p-6 hover:bg-gray-200 transition text-blue-600"
            >
              <Icon name="mdi:music" class="mr-2" />
              Écouter la musique
            </a>
            <p v-else class="block p-6 text-gray-400">Musique non disponible</p>
          </div>
        </section>

        <!-- Chorégraphie -->
        <section>
          <h2 class="text-2xl font-semibold mb-4">Chorégraphie</h2>
          <div class="space-y-4">
            <!-- Vidéo -->
            <a
              v-if="danse?.videoUrl"
              :href="danse.videoUrl"
              target="_blank"
              class="block bg-gray-100 rounded-xl p-6 hover:bg-gray-200 transition"
            >
              <div class="flex items-center justify-center">
                <Icon name="mdi:video" class="mr-2" />
                Vidéo de chorégraphie
              </div>
            </a>
            <p v-else class="block p-6 text-gray-400">Vidéo non disponible</p>

            <!-- PDF -->
            <a
              v-if="danse?.pdfUrl"
              :href="danse.pdfUrl"
              target="_blank"
              class="block bg-gray-100 rounded-xl p-6 hover:bg-gray-200 transition"
            >
              <div class="flex items-center justify-center">
                <Icon name="mdi:file-pdf-box" class="mr-2" />
                PDF de chorégraphie
              </div>
            </a>
            <p v-else class="block p-6 text-gray-400">PDF non disponible</p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute();
const { data: danses } = await useFetch<Danse[]>(`/cache/danses.json`);

const danse = computed(
  () => danses.value?.find((d) => d.id === route.params.id) ?? null
);

useHead({
  title: `${danse.value.nom} - DML Laillé`,
  meta: [
    {
      name: "description",
      content: `Découvrez la danse ${danse.value.nom} et apprenez ses chorégraphies à Laillé (35).`,
    },
    { property: "og:title", content: `${danse.value.nom} - DML Laillé` },
    {
      property: "og:description",
      content: `Découvrez la danse ${danse.value.nom} et apprenez ses chorégraphies à Laillé (35).`,
    },
    { property: "og:type", content: "article" },
    {
      property: "og:url",
      content: `https://dml-country/danses/${route.params.id}`,
    },
  ],
});
</script>
