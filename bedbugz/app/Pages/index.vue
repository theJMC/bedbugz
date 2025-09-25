<template>
    <div class="main-background homepage">
        <div class="homepage-title"> 
            <h1 class="font-semibold font-white font-32"> BedBugZ </h1>
            <h2 class="font-medium font-grad font-20"> bug bites to love bites </h2>
        </div>
        <div class="homepage-buttons">
            <ButtonElement 
                icon="favorite"
                text="find a match"
                @click="handleFindAMatch"
            />
            <ButtonElement 
                icon="park"
                text="view date spots"
                @click="handleViewDates"
            />
            <ButtonElement 
                icon="pest_control"
                text="scan a suitor"
                @click="handleScanSuitor"
            />
        </div>
        <PercentBar 
            :number="completionNumber"
        />
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';
import PercentBar from '~/components/percent.vue';

export default {
    components: {
        ButtonElement,
        PercentBar
    },
    data() {
        return {
            completionNumber: 0
        }
    },
    mounted() {
        // on page load get complete % from somewhere
        this.completionNumber = 33;
    },
    methods: {
        handleFindAMatch() {
            this.$router.push('/suitors');
        },
        handleViewDates() {
            console.log('go to view dates')
        },
        handleScanSuitor() {
            console.log('go to scan suitor')
        },
    }
}
</script>

<style lang="scss">
.homepage {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    &-title {
        margin-top: 70px;
        text-align: center;
    }

    &-buttons {
        width: 75%;

    }
}
</style>