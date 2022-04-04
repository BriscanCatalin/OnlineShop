<template>
    <app-layout title="Products">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                Contact Us
            </h2>
        </template>

        <div>
            <div class="antialiased bg-gray-100">
                <div
                    class="flex w-full min-h-screen justify-center items-center"
                >
                    <div
                        class="flex flex-col md:flex-row md:space-x-20 space-y-6 bg-cyan-700 w-full max-w-4xl p-8 sm:p-12 rounded-xl shadow-lg text-white overflow-hidden"
                    >
                        <div class="flex flex-col space-y-8 justify-between">
                            <div>
                                <h1 class="font-bold text-4xl tracking-wide">
                                    Contact Us
                                </h1>
                                <p class="pt-2 text-cyan-100 text-sm">
                                    Responsive contact form lorem ipsum
                                </p>
                            </div>
                            <div class="flex flex-col space-y-6">
                                <div class="inline-flex space-x-2 items-center">
                                    <ion-icon
                                        name="call"
                                        class="text-teal-300 text-xl"
                                    ></ion-icon>
                                    <span>(+40) 754 651 225 </span>
                                </div>
                                <div class="inline-flex space-x-2 items-center">
                                    <ion-icon
                                        name="mail"
                                        class="text-teal-300 text-xl"
                                    ></ion-icon>
                                    <span>cata.briscan@gmail.com</span>
                                </div>

                                <div class="inline-flex space-x-2 items-center">
                                    <ion-icon
                                        name="location"
                                        class="text-teal-300 text-xl"
                                    ></ion-icon>
                                    <span>Str. Sarmas Nr. 11C Zalau </span>
                                </div>
                            </div>
                            <div class="flex space-x-4 text-lg">
                                <a href="%">
                                    <ion-icon name="logo-facebook"></ion-icon>
                                </a>
                                <a href="%">
                                    <ion-icon name="logo-instagram"></ion-icon>
                                </a>
                                <a href="%">
                                    <ion-icon name="logo-linkedin"></ion-icon>
                                </a>
                                <a href="%">
                                    <ion-icon name="logo-google"></ion-icon>
                                </a>
                            </div>
                        </div>
                        <div class="relative">
                            <div class="absolute z-0 w-40 h-40 bg-teal-400 rounded-full -right-28 -top-28"></div>
                            <div class="absolute z-0 w-40 h-40 bg-teal-400 rounded-full -left-8 -bottom-28"></div>
                            <div
                                class="relative z-10 bg-white rounded-xl shadow-lg p-8 text-gray-600 md:w-auto md:ml-20"
                            >
                                <form action="" @submit="sendEmail" class="flex flex-col space-y-4">
                                    <div>
                                        <label for="" class="text-sm"
                                            >Your name</label
                                        >
                                        <input
                                            type="text"
                                            placeholder="Your name"
                                            v-model="name"
                                            class="ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300"
                                        />
                                    </div>
                                    <div>
                                        <label for="" class="text-sm"
                                            >Email Address</label
                                        >
                                        <input
                                            type="email"
                                            v-model="email"
                                            placeholder="Email Address"
                                            class="ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300"
                                        />
                                    </div>
                                    <div>
                                        <label for="" class="text-sm"
                                            >Message</label
                                        >
                                        <textarea
                                            placeholder="Message"
                                            v-model="message"
                                            rows="4"
                                            class="ring-1 ring-gray-300 w-full rounded-md px-4 py-2 mt-2 outline-none focus:ring-2 focus:ring-teal-300"
                                        />
                                    </div>
                                    <button
                                        class="inline-block self-end bg-cyan-700 text-white font-bold rounded-lg px-2 py-2 uppercase text-sm"
                                        type="submit"
                                    >
                                        Send Message
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </app-layout>
</template>

<script>
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";
import JetSectionBorder from "@/Jetstream/SectionBorder.vue";
import { createStore } from 'vuex'

const store = createStore({
  state () {
    return {
      count: 0
    }
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

export default defineComponent({
    props: ["sessions"],

    components: {
        AppLayout,
        JetSectionBorder,
    },
    data() {
        return {
            name: '',
            email: '',
            message: ''
        }
    },
    created() {
        var scripts = [
            "https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js",
        ];
        scripts.forEach((script) => {
            let tag = document.createElement("script");
            tag.setAttribute("src", script);
            document.head.appendChild(tag);
        });
    },
    methods: {
        sendEmail(e) {
           e.preventDefault();        
           fetch('http://127.0.0.1:5000/contact/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: this.name, 
                email: this.email, 
                message: this.message
            })

        }).then((response) => response.status)
            .then((status) => {
                if(status === 200){
                    console.log("Email send!");
                }
                return status;
            })
            .catch((error) => {
                console.error(error);
            });
        } 
    }
});
</script>
