<template>
    <section class="profile">
        <img />
        <div>
            <h1 class="font-white font-32 font-semibold"> Profile </h1>
            <h2 class="font-grad font-20"> View and edit your profile </h2>
        </div>
    </section>
</template>

<style lang="scss">
.profile{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>

<script lang="js">
export default {
    name: "ProfileElement",
    props: {
        images: {
            type: String
        },
        text: {
            type: String, 
            default: ''
        }
    }
}
</script>