<template>
  <div class="bg-white text-gray-800">
    <div
      class="bg-cover bg-center h-screen text-white"
      :style="{ backgroundImage: `url(${backgroundImagePath})` }"
    >
      <div
        class="bg-black bg-opacity-40 h-full flex flex-col justify-center items-center text-center px-4"
      >
        <h1 class="text-4xl md:text-6xl font-bold mb-4">
          Bienvenue à Danse et Musiques de Laille
        </h1>
        <p class="text-lg md:text-2xl mb-6">
          Cours, danses, événements… Vivez l'ambiance western !
        </p>
        <div>
          <NuxtLink
            to="cours"
            class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded mr-2"
          >
            Consulter les cours
          </NuxtLink>
          <NuxtLink
            to="agenda"
            class="bg-transparent border border-white hover:bg-white hover:text-black text-white font-bold py-2 px-4 rounded"
          >
            Consulter l'agenda
          </NuxtLink>
        </div>
      </div>
    </div>

    <!-- Cours Section -->
    <section id="cours" class="py-16 px-4 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold text-center mb-4">Nos Cours</h2>
      <p class="text-center mb-4">
        Les cours de country se déroulent à la salle du Boulais, 39 rue de la
        Halte, 35890 Laillé
      </p>
      <div class="grid md:grid-cols-4 gap-6">
        <div
          v-for="details in detailsDesCoursCountry"
          :key="details.niveau"
          class="bg-gray-100 p-6 rounded-lg shadow-md"
        >
          <h4 class="text-xl font-semibold mb-2 flex items-center">
            {{ details.niveau }}
          </h4>
          <p>{{ details.horaire }}</p>
          <p class="mt-2 text-sm">{{ details.description }}</p>
        </div>
      </div>
      <div class="text-center mt-6">
        <NuxtLink to="/cours" class="text-blue-600 underline">
          Voir tous les cours
        </NuxtLink>
      </div>
    </section>

    <!-- Danses Section -->
    <section id="danses" class="py-16 bg-gray-50 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center mb-8">Les Danses</h2>
        <div class="grid md:grid-cols-4 gap-4">
          <div class="bg-white p-4 rounded shadow text-center">Country</div>
          <div class="bg-white p-4 rounded shadow text-center">Line</div>
          <div class="bg-white p-4 rounded shadow text-center">Catalan</div>
          <div class="bg-white p-4 rounded shadow text-center">Celtique</div>
        </div>
        <div class="text-center mt-6">
          <NuxtLink to="/danses" class="text-blue-600 underline">
            Voir toutes les danses
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts" setup>
import backgroundImagePath from "~/static/images/home.jpg";

const detailsDesCoursCountry = [
  {
    niveau: "Débutants",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse country.Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la country, ou n'en avez jamais fait, alors il est fait pour vous.",
    horaire: "Mercredi 18h15 - 19h10",
  },
  {
    niveau: "Novice",
    description:
      "Ce cours s’adresse aux personnes qui veulent découvrir de nouvelles chorégraphies tout en travaillant avec des techniques et des rythmes encore plus variés.",
    horaire: "Mercredi 19h15 - 20h25",
  },
  {
    niveau: "Intermédiaire",
    description:
      "Ce cours s’adresse aux personnes qui souhaitent acquérir des chorégraphiques techniques sur des rythmes plus difficiles.",
    horaire: "Mercredi 20h30 – 21h45",
  },
  {
    niveau: "Intermédiaire +",
    description:
      "Ce cours s’adresse aux personnes qui souhaitent acquérir des chorégraphiques techniques sur des rythmes plus difficiles.",
    horaire: "Mercredi 21h15 - 22h00",
  },
];
</script>

<style>
</style>