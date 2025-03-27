<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-800 mb-6">1.2.3. Whiskey</h1>

      <div class="grid md:grid-cols-2 gap-8">
        <!-- Section Média -->
        <div>
          <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Musique</h2>
            <div class="bg-gray-100 rounded-lg p-4">
              <a
                :href="danse?.lien_musique"
                target="_blank"
                rel="noopener noreferrer"
                class="text-blue-600 hover:underline flex items-center"
              >
                <Icon name="mdi:music" class="mr-2" />
                <span v-if="danse?.lien_musique"> Écouter la musique </span>
                <span v-else class="text-gray-400">Non disponible</span>
              </a>
            </div>
          </div>

          <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Chorégraphie</h2>
            <div class="space-y-4">
              <a
                :href="danse?.video_choregraphie"
                target="_blank"
                class="block bg-gray-100 rounded-lg p-4 hover:bg-gray-200 transition"
              >
                <div class="flex items-center">
                  <Icon name="mdi:video" class="mr-2" />
                  <span v-if="danse?.video_choregraphie">
                    Vidéo de chorégraphie
                  </span>
                  <span v-else class="text-gray-400">Non disponible</span>
                </div>
              </a>

              <a
                :href="danse?.pdf_choregraphie"
                target="_blank"
                class="block bg-gray-100 rounded-lg p-4 hover:bg-gray-200 transition"
              >
                <div class="flex items-center">
                  <Icon name="mdi:file-pdf-box" class="mr-2" />
                  <span v-if="danse?.pdf_choregraphie">
                    PDF de chorégraphie
                  </span>
                  <span v-else class="text-gray-400">Non disponible</span>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- Section Détails -->
        <div>
          <div class="bg-white shadow-md rounded-lg p-6">
            <h2 class="text-xl font-semibold mb-4 border-b pb-2">
              Détails de la danse
            </h2>
            <div class="space-y-4">
              <div>
                <p class="text-gray-600 font-medium">Type de danse</p>
                <p>Country</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute();
const id = route.params.id as string;
console.log(id);
console.log(route.path);

const { data: danse } = await useAsyncData(route.path, () =>
  queryCollection("danses").path(route.path).first()
);
</script>

<style>
</style>