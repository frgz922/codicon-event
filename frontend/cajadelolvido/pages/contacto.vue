<template>
    <div class="container mx-auto pt-20">
        <h1 class="text-accent font-blackops text-2xl">Contacto</h1>
        <div class="grid grid-cols-2 items-center">
            <div class="font-blackops text-bkg font-bold text-lg gap-6 space-y-16">
                <div>Escribenos todas tus dudas y pregunta y nuestros agentes te respodera con gusto.</div>
                <div class="space-y-5">
                    <div class="text-sm flex gap-4">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5}
                            stroke="currentColor" class="w-6 h-6">
                            <path strokeLinecap="round" strokeLinejoin="round"
                                d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
                        </svg>
                        <span>+58 412 123 45 67</span>
                    </div>
                    <div class="text-sm flex gap-4">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
                        </svg>

                        <span>cajadelolvido@gmail.com</span>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-2 gap-7">
                <input type="text" placeholder="Nombre" v-model="name"
                    class="bg-gray-200 border-2 border-accent text-gray-800 placeholder-bkg text-sm rounded-lg focus:ring-bkg focus:border-bkg block w-full p-2.5">
                <input type="text" placeholder="Correo" v-model="email"
                    class="bg-gray-200 border-2 border-accent text-gray-800 placeholder-bkg text-sm rounded-lg focus:ring-bkg focus:border-bkg block w-full p-2.5">
                <textarea placeholder="Preguntanos lo que desees..." v-model="message" rows="10"
                    class="bg-gray-200 border-2 border-accent text-gray-800 placeholder-bkg text-sm rounded-lg focus:ring-bkg focus:border-bkg block w-full p-2.5 col-span-2"></textarea>
                <div @click="saveContact"
                    class="w-32 p-2 text-center font-blackops cursor-pointer rounded-full border-2 bg-gray-200 border-accent text-bkg hover:bg-accent hover:text-white">
                    Enviar</div>
            </div>
        </div>
        <TransitionRoot as="template" :show="show">
            <Dialog as="div" class="relative z-10" @close="() => show = false">
                <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                    leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                </TransitionChild>

                <div class="fixed inset-0 z-10 overflow-y-auto">
                    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                        <TransitionChild as="template" enter="ease-out duration-300"
                            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                            leave-from="opacity-100 translate-y-0 sm:scale-100"
                            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                            <DialogPanel
                                class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
                                <div>
                                    <div class="mt-3 text-center sm:mt-5">
                                        <DialogTitle as="h1" class="font-semibold text-lg text-accent font-blackops">
                                            Gracias por contactarnos
                                        </DialogTitle>
                                        <div class="mt-2 text-bkg text-center text-sm space-y-5 pt-6">
                                            <p>
                                                Hemos recibido tu mensaje, pronto nos pondremos en contacto contigo.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <div class="mt-5 sm:mt-6">
                                    <button type="button"
                                        class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                                        @click="() => show = false">Cerrar</button>
                                </div>
                            </DialogPanel>
                        </TransitionChild>
                    </div>
                </div>
            </Dialog>
        </TransitionRoot>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'

export default defineComponent({
    components: {
        Dialog,
        DialogPanel,
        DialogTitle,
        TransitionChild,
        TransitionRoot,
    },
    data() {
        return {
            name: '',
            email: '',
            message: '',
            uri: 'http://127.0.0.1:8000',
            show: false
        }
    },
    methods: {
        async saveContact() {
            const data = {
                name: this.name,
                email: this.email,
                message: this.message,
            }
            await fetch(`${this.uri}/contact/`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            }).then((response) => {
                if (response.status === 200 || response.status === 201) {
                    this.show = true
                }
            });
        }
    },
})
</script>

<style scoped></style>