import type { CoursCollectionItem } from "@nuxt/content";

export class Cours {
  collectionItem: CoursCollectionItem;
  dateRealisation: String;

  constructor(
    collectionItem: CoursCollectionItem,
  ) {
    this.collectionItem = collectionItem
    this.dateRealisation = new Date(collectionItem.date_realisation).toLocaleDateString("fr-FR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
    })
  }

  static dancePathToDanceName(dancePath: string): string {
    var sanitizedDanceName = dancePath.replaceAll("danses/", "").replaceAll("-", " ")
    return sanitizedDanceName.charAt(0).toUpperCase() + sanitizedDanceName.slice(1);
  }
}

export class CoursCollection {
  items: Cours[];

  constructor(items: Cours[]) {
    this.items = items;
  }

  static fromCoursCollectionItems(courssCollectionItems: CoursCollectionItem[] | null) {
    return new CoursCollection(courssCollectionItems?.map((coursCollectionItem: CoursCollectionItem) =>
      new Cours(coursCollectionItem)
    ) ?? []);
  }
}