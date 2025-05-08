<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-800 mb-6">
        {{ danse.collectionItem.nom }}
      </h1>

      <div class="grid md:grid-cols-2 gap-8">
        <div>
          <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Musique</h2>
            <div class="bg-gray-100 rounded-lg p-4">
              <a
                v-if="danse.collectionItem.lien_musique"
                :href="danse.collectionItem.lien_musique"
                target="_blank"
                rel="noopener noreferrer"
                class="text-blue-600 hover:underline flex items-center"
              >
                <Icon name="mdi:music" class="mr-2" />
                <span> Écouter la musique </span>
              </a>
              <span v-else class="text-gray-400">Non disponible</span>
            </div>
          </div>

          <div class="mb-6">
            <h2 class="text-xl font-semibold mb-4">Chorégraphie</h2>
            <div class="space-y-4">
              <a
                v-if="danse.collectionItem.lien_video_choregraphie"
                :href="danse.collectionItem.lien_video_choregraphie"
                target="_blank"
                class="block bg-gray-100 rounded-lg p-4 hover:bg-gray-200 transition"
              >
                <div class="flex items-center">
                  <Icon name="mdi:video" class="mr-2" />
                  <span> Vidéo de chorégraphie </span>
                </div>
              </a>
              <span v-else class="text-gray-400">Non disponible</span>

              <a
                v-if="danse.collectionItem.lien_pdf_choregraphie"
                :href="danse.collectionItem.lien_pdf_choregraphie"
                target="_blank"
                class="block bg-gray-100 rounded-lg p-4 hover:bg-gray-200 transition"
              >
                <div class="flex items-center">
                  <Icon name="mdi:file-pdf-box" class="mr-2" />
                  <span> PDF de chorégraphie </span>
                </div>
              </a>
              <span v-else class="text-gray-400">Non disponible</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { Danse } from "~/models";

const route = useRoute();
const { data, error } = await useAsyncData(route.path, () =>
  queryCollection("danses").path(route.path).first()
);
if (error) {
  console.log(error.value);
}
const danse = new Danse(data.value!);
</script>

<style>
</style>