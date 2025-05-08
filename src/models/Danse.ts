import type { DansesCollectionItem, PageCollectionItemBase } from "@nuxt/content";

export class Danse {
  collectionItem: DansesCollectionItem;

  constructor(
    collectionItem: DansesCollectionItem,
  ) {
    this.collectionItem = collectionItem
  }
}

export class DanseCollection {
  items: Danse[];

  constructor(items: Danse[]) {
    this.items = items;
  }

  static fromDansesCollectionItems(dansesCollectionItems: DansesCollectionItem[] | null) {
    return new DanseCollection(dansesCollectionItems?.map((danseCollectionItem: DansesCollectionItem) =>
      new Danse(danseCollectionItem)
    ) ?? []);
  }

  getBySearchQuery(searchQuery: string) {
    return this.items.filter(danse =>
      danse.collectionItem.nom.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }
}