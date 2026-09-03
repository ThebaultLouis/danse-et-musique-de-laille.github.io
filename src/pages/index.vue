<template>
  <div class="bg-background text-foreground">
    <div class="relative h-screen min-h-[36rem] overflow-hidden text-white">
      <picture>
        <source
          type="image/webp"
          srcset="
            /fichiers/images/home-640.webp   640w,
            /fichiers/images/home-1280.webp 1280w,
            /fichiers/images/home-1920.webp 1920w,
            /fichiers/images/home-3000.webp 3000w
          "
          sizes="100vw"
        >
        <img
          src="/fichiers/images/home.jpg"
          alt=""
          width="3000"
          height="2000"
          fetchpriority="high"
          decoding="async"
          class="absolute inset-0 h-full w-full object-cover"
        >
      </picture>
      <div
        class="relative h-full flex flex-col justify-center items-center bg-gradient-to-b from-foreground-dark/50 via-black/30 to-foreground-dark/70 text-center px-4 pt-20"
      >
        <h1
          class="max-w-5xl text-4xl sm:text-5xl md:text-6xl font-bold leading-tight drop-shadow-lg mb-4"
        >
          Bienvenue à Danse et Musiques de Laille
        </h1>
        <p class="text-lg md:text-2xl drop-shadow-md mb-8">
          Cours, danses, événements… Vivez l'ambiance western !
        </p>
        <div
          class="flex flex-col sm:flex-row sm:space-x-2 space-y-2 sm:space-y-0"
        >
          <NuxtLink
            to="cours"
            class="bg-secondary hover:bg-secondary-light text-foreground-dark font-bold py-3 px-6 rounded-lg shadow-lg transition-colors"
          >
            Consulter les cours
          </NuxtLink>
          <NuxtLink
            to="agenda"
            class="bg-background/10 border border-background/80 hover:bg-background hover:text-foreground-dark text-white font-bold py-3 px-6 rounded-lg backdrop-blur-sm transition-colors"
          >
            Consulter l'agenda
          </NuxtLink>
        </div>
      </div>
    </div>

    <!-- Cours Section -->
    <section id="cours" class="py-16 px-4 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold text-center mb-4">Nos Cours</h2>
      <div
        v-for="jour in new Set(detailsDesCoursCountry.map((c) => c.jour))"
        :key="jour"
        class="py-4"
      >
        <p class="text-center mb-4 text-2xl">{{ jour }}</p>
        <p class="text-center mb-4 text-foreground-subtle">
          {{ lieux.find((l) => l.jour === jour)?.lieu }}
        </p>
        <div class="grid lg:grid-cols-3 gap-6">
          <div
            v-for="details in detailsDesCoursCountry.filter(
              (c) => c.jour == jour
            )"
            :key="`${details.type}-${details.horaire}`"
            class="bg-surface border border-outline p-6 rounded-xl shadow-md space-y-3"
          >
            <div>
              <h3 class="text-2xl font-semibold text-foreground">
                {{ details.type }}
              </h3>
              <h4 v-if="details.niveau" class="text-lg text-foreground-subtle">
                Niveau : {{ details.niveau }}
              </h4>
              <p v-if="details.frequence" class="text-lg text-foreground-subtle">
                {{ details.frequence }}
              </p>
            </div>

            <!-- Schedule + animateur -->
            <div class="text-sm text-foreground-subtle space-y-1">
              <p>{{ details.horaire }}</p>
              <p v-if="details.animateur">
                Animé par
                <span class="font-medium text-foreground-muted">{{
                  details.animateur
                }}</span>
              </p>
            </div>

            <!-- Description -->
            <p
              v-if="details.description"
              class="text-base text-foreground-muted leading-relaxed"
            >
              {{ details.description }}
            </p>
          </div>
        </div>
      </div>

      <div class="text-center mt-6">
        <NuxtLink
          to="/cours"
          class="font-semibold text-primary hover:text-primary-dark underline"
        >
          Voir tous les cours
        </NuxtLink>
      </div>
    </section>

    <section
      class="max-w-6xl mx-auto bg-surface-muted border-l-4 border-primary rounded-xl p-8 text-center shadow-sm"
    >
      <h2 class="text-2xl font-bold text-foreground mb-4">
        Prêt à vous inscrire ?
      </h2>
      <p class="text-foreground-muted mb-6">
        Téléchargez le formulaire, remplissez-le et envoyez-le à
        <a
          href="mailto:countrydanselaille@gmail.com"
          class="font-medium text-primary hover:text-primary-dark"
          >countrydanselaille@gmail.com</a
        >
        ou imprimer le et donner le directement à votre prochain cours
      </p>
      <a
        href="/fichiers/inscriptions/2026-2027.pdf"
        target="_blank"
        class="inline-block bg-primary hover:bg-primary-dark text-white font-semibold px-6 py-3 rounded-lg shadow-md transition"
      >
        📄 Télécharger le formulaire
      </a>
    </section>

    <section
      class="max-w-6xl mx-auto my-8 bg-surface border-l-4 border-secondary rounded-xl p-8 shadow-sm"
    >
      <!-- Titre -->
      <h2 class="text-3xl font-bold text-center mb-4">Contactez-nous</h2>

      <!-- Introduction -->
      <p class="text-foreground-muted mb-6 text-center">
        Vous pouvez nous informer de votre événement en nous envoyant un mail à
        :
      </p>

      <!-- Informations -->
      <div class="text-center mb-6">
        <div>
          <h3 class="text-lg font-semibold text-foreground mb-1">
            Informations générales
          </h3>
          <a
            href="mailto:countrydanselaille@gmail.com"
            class="text-primary hover:text-primary-dark hover:underline"
          >
            countrydanselaille@gmail.com
          </a>
        </div>
        <div class="mt-4">
          <h3 class="text-lg font-semibold text-foreground mb-1">
            Organisation des événements
          </h3>
          <a
            href="mailto:valeriedml35@gmail.com"
            class="text-primary hover:text-primary-dark hover:underline"
          >
            valeriedml35@gmail.com
          </a>
        </div>
      </div>

      <!-- Closing -->
      <p class="text-foreground-muted text-center">
        Avec plaisir de vous retrouver sur la piste de danse ! 🎶💃
      </p>
    </section>

    <section class="bg-surface-muted p-8 space-y-8">
      <!-- Titre principal -->
      <h2 class="text-3xl font-bold text-foreground text-center mb-6">
        À propos de DML Laillé
      </h2>

      <!-- Animateurs -->
      <div class="space-y-2 text-center">
        <h3 class="text-2xl font-semibold text-foreground-muted">Animateurs DML</h3>
        <div class="flex flex-col sm:flex-row justify-center gap-8 pt-4">
          <figure class="flex flex-col items-center gap-3">
            <img
              src="/fichiers/images/animateur-valerie.jpg"
              alt="Valérie, animatrice DML"
              class="w-40 h-40 rounded-full object-cover shadow-md"
            >
            <figcaption class="text-lg font-medium text-foreground-muted">
              Valérie
            </figcaption>
          </figure>
          <figure class="flex flex-col items-center gap-3">
            <img
              src="/fichiers/images/animateur-chouchou.jpg"
              alt="Chouchou, animateur DML"
              class="w-40 h-40 rounded-full object-cover shadow-md"
            >
            <figcaption class="text-lg font-medium text-foreground-muted">
              Chouchou
            </figcaption>
          </figure>
        </div>
      </div>

      <!-- La danse -->
      <div class="space-y-2 max-w-6xl mx-auto">
        <h3 class="text-2xl font-semibold text-foreground-muted">La danse</h3>
        <p class="text-foreground-muted leading-relaxed">
          La danse est un excellent moyen de vous évader. Grâce à cette
          discipline, vous avez la capacité de vous libérer et de laisser libre
          cours au bien-être.
        </p>
        <p class="text-foreground-muted leading-relaxed">
          Les cours de danse sont assurés par des animateurs bénévoles et
          investis.
        </p>
        <p class="text-foreground-muted leading-relaxed">
          Quoi de mieux que d'opter pour de la danse country pratiquée à Laillé
          (35) sur tous styles de musique : Country, Catalan, Celtique, New
          Country, Line, Danse en couple, Danse en contrat.
        </p>
      </div>

      <!-- Événements et manifestations -->
      <div class="space-y-2 max-w-6xl mx-auto">
        <h3 class="text-2xl font-semibold text-foreground-muted">
          Événements et manifestations
        </h3>
        <ul
          class="list-disc list-inside text-foreground-muted leading-relaxed space-y-1"
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

const lieux = [
  {
    jour: "Mercredi",
    lieu: "Salle de L’Archipel, rue du commandant Cousteau, 35890 Laillé",
  },
  {
    jour: "Jeudi",
    lieu: "Salle du point 21, 21 rue du Point du jour, 35890 Laillé",
  },
  {
    jour: "Vendredi",
    lieu: "Salle des Boulais, 35890 Laillé",
  },
];

interface DetailsCours {
  type: string;
  niveau?: string;
  frequence?: string;
  description?: string;
  jour: string;
  horaire: string;
  animateur?: string;
}

const detailsDesCoursCountry: DetailsCours[] = [
  {
    type: "Country",
    niveau: "Débutant + Novice",
    description:
      "Ce cours s’adresse aux personnes qui veulent découvrir la danse Country et de nouvelles chorégraphies.",
    jour: "Mercredi",
    horaire: "18h30 - 20h00",
    animateur: "Valérie",
  },
  {
    type: "Country",
    niveau: "Intermédiaire",
    description:
      "Ce cours s’adresse aux personnes qui souhaitent acquérir des chorégraphiques techniques sur des rythmes plus difficiles.",
    jour: "Mercredi",
    horaire: "20h30 – 22h00",
    animateur: "Valérie",
  },
  {
    type: "Country",
    niveau: "Débutant",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse Country. Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la Country, ou n'en avez jamais fait, alors il est fait pour vous.",
    jour: "Jeudi",
    horaire: "18h30 - 19h30",
    animateur: "Valérie",
  },
  {
    type: "Catalan",
    niveau: "Débutant",
    description:
      "Ce cours s'adresse aux personnes qui veulent découvrir la danse Catalan. Les danses sont simples pour acquérir les bases des pas. Si vous découvrez tout juste la country, ou n'en avez jamais fait, alors il est fait pour vous.",
    jour: "Jeudi",
    horaire: "19h45 - 20h45",
    animateur: "Chouchou",
  },
  {
    type: "Catalan",
    niveau: "Novice + Intermédiaire",
    description:
      "Ce cours s’adresse aux personnes qui veulent découvrir de nouvelles chorégraphies tout en travaillant avec des techniques et des rythmes encore plus variés.",
    jour: "Jeudi",
    horaire: "20h50 - 22h00",
    animateur: "Chouchou",
  },
  {
    type: "Cours Vintage",
    niveau: "Tous niveaux",
    frequence: "1er vendredi, semaine impaire",
    description: "Apprendre des danses qui ont plus de 5 ans.",
    jour: "Vendredi",
    horaire: "18h30 - 22h00",
    animateur: "Valérie et Chouchou",
  },
  {
    type: "Soirée conviviale",
    niveau: "Tous niveaux",
    frequence: "2ème vendredi, semaine impaire",
    description:
      "Ouverte à tous les adhérents et invités, avec une playlist faite par les adhérents.",
    jour: "Vendredi",
    horaire: "18h30 - 24h00",
    animateur: "Valérie et Chouchou",
  },
];
</script>

<style>
</style>
