/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />

declare global {
  interface Window {
    __swRegistered?: boolean;
    __swRegisterPromise?: Promise<ServiceWorkerRegistration | null> | null;
    __swipeListenerAttached?: boolean;
    __menuListenerAttached?: boolean;
    __flipCardsListenerAttached?: boolean;
  }
}

export {};