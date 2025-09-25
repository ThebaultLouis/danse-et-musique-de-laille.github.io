<template>
  <div class="bg-white text-gray-800">
    <div
      class="bg-cover bg-center h-screen text-white"
      :style="{ backgroundImage: `url(fichiers/images/home.jpg)` }"
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
        <div
          class="flex flex-col sm:flex-row sm:space-x-2 space-y-2 sm:space-y-0"
        >
          <NuxtLink
            to="cours"
            class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded"
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
        Les cours de country se déroulent à la salle du point 21, 39 rue de la
        Halte, 35890 Laillé
      </p>
      <div
        v-for="jour in new Set(detailsDesCoursCountry.map((c) => c.jour))"
        :key="jour"
        class="py-4"
      >
        <p class="text-center mb-4 text-2xl">{{ jour }}</p>
        <div class="grid lg:grid-cols-3 gap-6">
          <div
            v-for="details in detailsDesCoursCountry.filter(
              (c) => c.jour == jour
            )"
            :key="details.niveau"
            class="bg-gray-100 p-6 rounded-lg shadow-md space-y-3"
          >
            <div>
              <h3 class="text-2xl font-semibold text-gray-800">
                {{ details.type }}
              </h3>
              <h4 class="text-lg text-gray-600">
                Niveau : {{ details.niveau }}
              </h4>
            </div>

            <!-- Schedule + animateur -->
            <div class="text-sm text-gray-500 space-y-1">
              <p>{{ details.horaire }}</p>
              <p>
                Animé par
                <span class="font-medium text-gray-700">{{
                  details.animateur
                }}</span>
              </p>
            </div>

            <!-- Description -->
            <p class="text-base text-gray-700 leading-relaxed">
              {{ details.description }}
            </p>
          </div>
        </div>
      </div>

      <div class="text-center mt-6">
        <NuxtLink to="/cours" class="text-blue-600 underline">
          Voir tous les cours
        </NuxtLink>
      </div>
    </section>

    <section
      class="bg-blue-50 border-l-4 border-blue-400 rounded-lg p-8 text-center"
    >
      <h2 class="text-2xl font-bold text-blue-800 mb-4">
        Prêt à vous inscrire ?
      </h2>
      <p class="text-gray-700 mb-6">
        Téléchargez le formulaire, remplissez-le et envoyez-le à
        <a href="mailto:countrydanselaille@gmail.com" class="text-blue-800"
          >countrydanselaille@gmail.com</a
        >
        ou imprimer le et donner le directement à votre prochain cours
      </p>
      <a
        href="/fichiers/inscriptions/2025-2026.pdf"
        target="_blank"
        class="inline-block bg-blue-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-blue-700 transition"
      >
        📄 Télécharger le formulaire
      </a>
    </section>

    <section class="border-l-4 rounded-lg p-8">
      <!-- Titre -->
      <h2 class="text-3xl font-bold text-center mb-4">Contactez-nous</h2>

      <!-- Introduction -->
      <p class="text-gray-700 mb-6 text-center">
        Vous pouvez nous informer de votre événement en nous envoyant un mail à
        :
      </p>

      <!-- Informations -->
      <div class="text-center mb-6">
        <div>
          <h3 class="text-lg font-semibold text-gray-800 mb-1">
            Informations générales
          </h3>
          <a
            href="mailto:countrydanselaille@gmail.com"
            class="text-blue-600 hover:underline"
          >
            countrydanselaille@gmail.com
          </a>
        </div>
        <div class="mt-4">
          <h3 class="text-lg font-semibold text-gray-800 mb-1">
            Organisation des événements
          </h3>
          <a
            href="mailto:valeriedml35@gmail.com"
            class="text-blue-600 hover:underline"
          >
            valeriedml35@gmail.com
          </a>
        </div>
      </div>

      <!-- Closing -->
      <p class="text-gray-700 text-center">
        Avec plaisir de vous retrouver sur la piste de danse ! 🎶💃
      </p>
    </section>

    <section class="bg-gray-50 rounded-lg p-8 space-y-8">
      <!-- Titre principal -->
      <h2 class="text-3xl font-bold text-gray-800 text-center mb-6">
        À propos de DML Laillé
      </h2>

      <!-- Animateurs -->
      <div class="space-y-2 text-center">
        <h3 class="text-2xl font-semibold text-gray-700">Animateurs DML</h3>
        <p class="text-gray-600">Valerie & Chouchou</p>
      </div>

      <!-- La danse -->
      <div class="space-y-2 max-w-6xl mx-auto">
        <h3 class="text-2xl font-semibold text-gray-700">La danse</h3>
        <p class="text-gray-700 leading-relaxed">
          La danse est un excellent moyen de vous évader. Grâce à cette
          discipline, vous avez la capacité de vous libérer et de laisser libre
          cours au bien-être.
        </p>
        <p class="text-gray-700 leading-relaxed">
          Les cours de danse sont assurés par des animateurs bénévoles et
          investis.
        </p>
        <p class="text-gray-700 leading-relaxed">
          Quoi de mieux que d'opter pour de la danse country pratiquée à Laillé
          (35) sur tous styles de musique : Country, Catalan, Celtique, New
          Country, Line, Danse en couple, Danse en contrat.
        </p>
      </div>

      <!-- Événements et manifestations -->
      <div class="space-y-2 max-w-6xl mx-auto">
        <h3 class="text-2xl font-semibold text-gray-700">
          Événements et manifestations
        </h3>
        <ul
          class="list-disc list-inside text-gray-700 leading-relaxed space-y-1"
        >
          <li>En décembre : Le bal du Père Noël.</li>
          <li>
            Engagement solidaire : DML Laillé 35 contribue à aider d’autres
            associations caritatives.
          </li>
          <li>
            Animations : DML Laillé 35 anime dans les clubs de la région ou dans
            des festivals.
          </li>
          <li>
            Participation : DML Laillé 35 participe aussi aux manifestations des
            autres associations.
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script lang="ts" setup>
useHead({
  title: "Accueil - DML Country",
  meta: [
    {
      name: "description",
      content: "Découvrez nos cours et événements de danse",
    },
  ],
});

const detailsDesCoursCountry = [
  {
    type: "Country",
    niveau: "Débutants",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse Country. Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la Country, ou n'en avez jamais fait, alors il est fait pour vous.",
    jour: "Mercredi",
    horaire: "18h15 - 19h10",
    animateur: "Valérie",
  },
  {
    type: "Country",
    niveau: "Novice",
    description:
      "Ce cours s’adresse aux personnes qui veulent découvrir de nouvelles chorégraphies tout en travaillant avec des techniques et des rythmes encore plus variés.",
    jour: "Mercredi",
    horaire: "19h15 - 20h30",
    animateur: "Valérie",
  },
  {
    type: "Country",
    niveau: "Intermédiaire",
    description:
      "Ce cours s’adresse aux personnes qui souhaitent acquérir des chorégraphiques techniques sur des rythmes plus difficiles.",
    jour: "Mercredi",
    horaire: "Mercredi 20h40 – 22h00",
    animateur: "Valérie",
  },
  {
    type: "Country",
    niveau: "Ultra débutant",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse Country. Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la Country, ou n'en avez jamais fait, alors il est fait pour vous.",
    jour: "Jeudi",
    horaire: "18h15 - 19h10",
    animateur: "Valérie",
  },
  {
    type: "Catalan",
    niveau: "Débutant",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse Catalan. Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la country, ou n'en avez jamais fait, alors il est fait pour vous.",
    jour: "Jeudi",
    horaire: "19h30 - 20h20",
    animateur: "Chouchou",
  },
  {
    type: "Catalan",
    niveau: "Novice - Intermédiaire",
    description:
      "Ce cours s’adresse aux personnes qui veulent découvrir de nouvelles chorégraphies tout en travaillant avec des techniques et des rythmes encore plus variés.",
    jour: "Jeudi",
    horaire: "20h30 - 22h00",
    animateur: "Chouchou",
  },
];
</script>

<style>
</style>