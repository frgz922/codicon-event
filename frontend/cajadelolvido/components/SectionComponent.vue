<template>
    <div :class="`bg-${background}`" class="h-screen pt-32">
        <div class="container mx-auto grid grid-cols-2 gap-96 items-center justify-center">
            <section>
                <div :class="{
                    'text-bkg': color === 'bkg',
                    'text-white': color === 'white'
                }">
                    <div class="font-blackops  -mt-64">
                        <span class="text-[610px]">{{ letter }}</span>
                        <span class="text-[100px] text-light">{{ word }}</span>
                    </div>
                    <p class="-mt-[12rem] text-[30px] font-bold text-justify">
                        {{ description }}
                    </p>
                </div>
            </section>
            <section>
                <slot name="content" />
            </section>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        background: {
            type: String,
            required: true
        },
        letter: {
            type: String,
            required: true
        },
        word: {
            type: String,
            required: true
        },
        description: {
            type: String,
            required: true
        },
        color: {
            type: String,
            required: true
        },
        img: {
            type: String,
            required: true
        }
    },
    setup() {
        return {}
    },

})
</script>

<style scoped></style>