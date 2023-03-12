<template>
  <div>
    <div class="overflow-hidden bg-bkg min-h-[calc(100vh_-_4rem)]">
      <div class="mx-auto grid grid-cols-2 justify-between items-center pt-16 gap-14 ml-[180px]">
        <div class="text-accent text-5xl font-blackops uppercase">
          <h1>Cierra Capitulos de tu vida</h1>
          <div class="text-purple-200 font-sans text-sm w-2/3 pt-6">
            Servicio para deshacerte de todo aquel recuerdo amargo que deseas eliminar
          </div>
          <div class="flex mt-20 gap-14">
            <div
              class="rounded-full bg-white font-blackops text-bkg uppercase text-sm px-4 py-2 hover:bg-accent hover:text-white">
              <NuxtLink to="#section">comienza ahora</NuxtLink>
            </div>
          </div>
        </div>

        <div class="bg-gray-300 rounded-l-full h-[688px]">
          <div class="grid grid-cols-2 grid-rows-2 box-border items-center mt-[50px] ml-[150px]">
            <div class="w-[400px]">
              <img src="~assets/images/caja-hero.png" alt="caja-hero" class="">
            </div>
            <div class="row-start-2 col-start-2 w-[390px]">
              <img src="~assets/images/caja-dos-hero.png" alt="caja-dos-hero">
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Carta -->
    <SectionComponent :img="sections.carta.img" :description="sections.carta.description"
      :background="sections.carta.background" :color="sections.carta.color" :letter="sections.carta.letter"
      :word="sections.carta.word" id="section">
      <template v-slot:content>
        <h1 class="text-accent font-sans text-lg font-bold uppercase pb-5 text-center">
          Escribe tu carta en la caja de abajo
        </h1>
        <textarea v-model="letter" placeholder="Escribe tu carta" rows="20"
          class="w-full rounded-md border-2 text-sm py-2 px-3.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-500 placeholder:text-gray-400 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      focus:ring-2 focus:ring-inset focus:ring-indigo-600"></textarea>
      </template>
    </SectionComponent>
    <!-- Archivo -->
    <SectionComponent :img="sections.archivar.img" :description="sections.archivar.description"
      :background="sections.archivar.background" :color="sections.archivar.color" :letter="sections.archivar.letter"
      :word="sections.archivar.word">
      <template v-slot:content>
        <h1 class="text-accent font-sans text-lg font-bold uppercase pb-5 text-center">
          Selecciona las fotos de aquello que quieres olvidar:
        </h1>
        <div>
          <input accept="image/*" capture multiple @change="onFileChanged"
            class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
            id="multiple_files" type="file">

          <div class="border-2 border-accent my-6"></div>

          <div class="overflow-y-auto h-[500px] collage">
            <div class="grid grid-cols-4">
              <img :src="imgSrc(file)" alt="" v-for="(file, index) in files" :key="index" class="w-32">
            </div>
          </div>
        </div>
      </template>
    </SectionComponent>
    <!-- Juntar -->
    <SectionComponent :img="sections.juntar.img" :description="sections.juntar.description"
      :background="sections.juntar.background" :color="sections.juntar.color" :letter="sections.juntar.letter"
      :word="sections.juntar.word">
      <template v-slot:content>
        <h1 class="text-accent font-sans text-lg font-bold uppercase pb-5 text-center">
          Selecciona tu caja de preferencia:
        </h1>
        <div class="grid grid-cols-2 gap-10 bg-slate-400 items-center p-4 rounded-md">
          <div class="flex flex-col items-center" v-for="boxItem in boxes" :key="boxItem.name">
            <div class="w-[150px] pb-2">
              <img :src="`/images/${boxItem.icon}`">
            </div>
            <div class="flex gap-4 items-center">
              <input type="radio" name="caja" :value="boxItem.name" v-model="box" :checked="box === boxItem.name">
              <label for="caja-dos" class="text-accent font-sans text-sm font-bold uppercase">{{ boxItem.name }} - ${{
                boxItem.price }} ({{ boxItem.dimensions }})</label>
            </div>
            <div class="uppercase text-bkg italic">
              <p>
                {{ boxItem.description }}
              </p>
            </div>
          </div>
        </div>
      </template>
    </SectionComponent>
    <!-- Arreglar -->
    <SectionComponent :img="sections.arreglar.img" :description="sections.arreglar.description"
      :background="sections.arreglar.background" :color="sections.arreglar.color" :letter="sections.arreglar.letter"
      :word="sections.arreglar.word">
      <template v-slot:content>
        <h1 class="text-accent font-sans text-lg font-bold uppercase pb-5 text-center">
          Selecciona de que manera deseas darle fin a estos recuerdos:
        </h1>
        <div class="grid grid-cols-2 gap-10 bg-slate-400 items-center p-4 rounded-md">
          <div class="flex flex-col items-center" v-for="serviceItem in services" :key="serviceItem.name">
            <div class="flex gap-4 items-center">
              <input type="radio" name="servicio" :value="serviceItem.name" v-model="service"
                :checked="service === serviceItem.name">
              <label for="caja-dos" class="text-accent font-sans text-sm font-bold uppercase">{{ serviceItem.name }} - ${{
                serviceItem.price }}</label>
            </div>
            <div class="uppercase text-bkg italic">
              <p>
                {{ serviceItem.description }}
              </p>
            </div>
          </div>
        </div>
      </template>
    </SectionComponent>
    <!-- Datos Personales -->
    <div class="bg-white space-y-20 h-full">
      <div>
        <h1 class="font-blackops text-bkg text-center text-2xl uppercase py-14">Datos Personales</h1>
        <div class="container mx-auto w-2/3 pt-5">
          <div class="flex flex-wrap justify-between gap-32">
            <div>
              <label class="font-blackops text-bkg text-lg">Nombre:</label>
              <input type="text" v-model="clientName"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div>
              <label class="font-blackops text-bkg text-lg">Apellido:</label>
              <input type="text" v-model="clientLastName"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div>
              <label class="font-blackops text-bkg text-lg">Correo:</label>
              <input type="text" v-model="clientEmail"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div>
              <label class="font-blackops text-bkg text-lg">Telefono:</label>
              <input type="text" v-model="clientPhone"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
          </div>
        </div>
      </div>
      <!-- Datos envio -->
      <div v-if="box === 'Regalo'" class="pb-10">
        <h1 class="font-blackops text-bkg text-center text-2xl uppercase py-14">¿A quien le enviaras tus
          recuerdos?</h1>
        <div class="container mx-auto w-2/3 pt-5">
          <div class="grid grid-cols-3 justify-between gap-32">
            <div>
              <label class="font-blackops text-bkg text-lg">Nombre:</label>
              <input type="text" v-model="recipientName"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div>
              <label class="font-blackops text-bkg text-lg">Apellido:</label>
              <input type="text" v-model="recipientLastName"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div>
              <label class="font-blackops text-bkg text-lg">Telefono:</label>
              <input type="text" v-model="recipientPhone"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50">
            </div>
            <div class="col-span-3">
              <label class="font-blackops text-bkg text-lg">Direccion:</label>
              <input type="text"
                class="text-black font-blackops peer h-full w-full border-b border-blue-gray-200 bg-transparent text-sm font-normal outline outline-0 transition-all placeholder-shown:border-blue-gray-200 focus:border-accent focus:outline-0 disabled:border-0 disabled:bg-blue-gray-50"
                v-model="recipientAddress" />
            </div>
          </div>
        </div>
      </div>
      <!--  -->
      <div class="container mx-auto pb-[100px]">
        <h1 class="font-blackops text-bkg text-center text-2xl uppercase py-14">Metodos de Pago</h1>
        <div class="grid grid-cols-3 text-center">
          <div class="flex flex-col font-blackops space-y-4">
            <h2 class="text-accent text-lg">Transferencia</h2>
            <div class="text-bkg text-sm flex flex-col gap-2">
              <span>Banco Mercantil</span>
              <span>Cta: 0105 1230 4567 890 9876</span>
              <span>C.I: 13 032 023</span>
              <span>Nombre: John Doe</span>
            </div>
          </div>
          <div class="flex flex-col font-blackops space-y-4">
            <h2 class="text-accent text-lg">Pago Movil</h2>
            <div class="text-bkg text-sm flex flex-col gap-2">
              <span>(0105)Mercantil</span>
              <span>C.I: 13 032 023</span>
              <span>Tlf: 0412 123 45 67</span>
            </div>
          </div>
          <div class="flex flex-col font-blackops space-y-4">
            <h2 class="text-accent text-lg">Zelle</h2>
            <div class="text-bkg text-sm flex flex-col gap-2">
              <span>cajadelolvido@gmail.coml</span>
            </div>
          </div>
        </div>
        <div class="flex justify-center gap-8 font-blackops items-center pt-20">
          <div class="text-xl flex flex-col">
            <label class="text-sm text-white">&nbsp;</label>
            <div><span class="text-bkg pr-2">Total:</span><span class="text-accent">
                ${{ total }}</span></div>
          </div>
          <div class="flex flex-col">
            <label class="text-sm text-bkg">NUMERO DE CONFIRMACION</label>
            <input type="text" placeholder="#00000000000" v-model="confirmationNumber"
              class="bg-gray-200 border-2 border-accent text-accent placeholder-gray-400 font-blackops text-sm rounded-lg focus:ring-bkg focus:border-bkg block w-full p-2.5">
          </div>
        </div>
        <div class="mt-24 flex justify-center">
          <div @click="complete"
            class="uppercase w-32 p-2 text-center font-blackops cursor-pointer rounded-full border-2 bg-bkg border-bkg text-white hover:bg-accent hover:text-white hover:border-accent">
            Pagar</div>
        </div>
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
                    <DialogTitle as="h1" class="font-semibold text-xl leading-6 text-accent font-blackops">
                      ¡Felicidades!
                    </DialogTitle>
                    <div class="mt-2 text-bkg text-center text-sm space-y-5 pt-6">
                      <p>Has completado tu C.A.J.A. del Olvido con exito.</p>
                      <p>Nuestros agentes de venta se estaran comunicando contigo una vez
                        confirmado el pago.</p>
                      <p>Deseamos que difrutes tu C.A.J.A. y tu vida tenga un inicio fresco.
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
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'


export default ({
  components: {
    Dialog,
    DialogPanel,
    DialogTitle,
    TransitionChild,
    TransitionRoot,
  },
  data() {
    return {
      loading: false,
      show: false,
      sections: {
        carta: {
          background: 'white',
          color: 'bkg',
          letter: 'C',
          word: 'arta',
          description: 'Aqui podras expresar todo aquello que tienes atascado en el pecho, decir todo lo que no se dijo sin ninguna excusa, desahogarte.',
          id: 'sectionC',
          img: 'carta.png',
        },
        archivar: {
          background: 'bkg',
          color: 'white',
          letter: 'A',
          word: 'rchivo',
          description: 'En esta seccion podras subir fotos de todos los malos recuerdos que seran destruidos en la caja del olvido.',
          id: 'sectionA',
          img: 'archivo.png',
        },
        juntar: {
          background: 'white',
          color: 'bkg',
          letter: 'J',
          word: 'untar',
          description: 'Aqui juntaras tu carta con las fotos para colocar luego en la caja de tu elección.',
          id: 'sectionJ',
          img: 'juntar.png',
        },
        arreglar: {
          background: 'bkg',
          color: 'white',
          letter: 'A',
          word: 'rreglar',
          description: 'Por ultimo, decidirás cual sera el final de esta caja del olvido que acabas de crear.',
          id: 'sectionA2',
          img: 'arreglar.png',
        }
      },
      letter: '',
      boxes: [] as any,
      services: [] as any,
      box: 'Ataud',
      service: 'Enterrar',
      media: [] as any,
      files: {} as FileList,
      clientName: '',
      clientLastName: '',
      clientEmail: '',
      clientPhone: '',
      confirmationNumber: '',
      uri: 'http://127.0.0.1:8000',
      recipientName: '',
      recipientLastName: '',
      recipientPhone: '',
      recipientAddress: '',
    }
  },
  beforeMount: async function () {
    const packages = await fetch(`${this.uri}/packages/`)
    const services = await fetch(`${this.uri}/services/`)
    this.boxes = await packages.json()
    this.services = await services.json()
  },
  methods: {
    onFileChanged($event: Event) {
      const target = $event.target as HTMLInputElement;

      if (target && target.files) {
        this.files = target.files;

        return target.files;
      }

    },
    imgSrc(file: File) {
      return URL.createObjectURL(file);
    },
    async complete() {
      var formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        formData.append('files[]', this.files[i]);
      }

      formData.append('clientName', this.clientName + ' ' + this.clientLastName);
      formData.append('clientEmail', this.clientEmail);
      formData.append('clientPhone', this.clientPhone);
      formData.append('letterContent', this.letter);
      formData.append('finalDestination', this.service.toLowerCase());
      formData.append('packageType', this.box.toLowerCase());
      formData.append('recipientName', this.recipientName + ' ' + this.recipientLastName);
      formData.append('recipientPhone', this.recipientPhone);
      formData.append('recipientAddress', this.recipientAddress);
      formData.append('confirmationNumber', this.confirmationNumber);


      await fetch(`${this.uri}/box/`, {
        method: "POST",
        body: formData

      }).then((response) => {
        if (response.status === 200 || response.status === 201) {
          this.show = true
          this.letter = ''
          this.clientName = ''
          this.clientLastName = ''
          this.clientEmail = ''
          this.clientPhone = ''
          this.confirmationNumber = ''
          this.recipientName = ''
          this.recipientLastName = ''
          this.recipientPhone = ''
          this.recipientAddress = ''
          this.files = {} as FileList
        }
      });
    },
  },
  computed: {
    boxPrice() {
      return this.boxes.length ? this.boxes.find((box: any) => box.name === this.box)?.price : 0
    },
    servicePrice() {
      return this.services.length ? this.services.find((service: any) => service.name === this.service)?.price : 0
    },
    total() {
      return this.boxPrice + this.servicePrice
    }
  }
})

</script>
