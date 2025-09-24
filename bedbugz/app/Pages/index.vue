<template>
    <div class="main-background">
        <div> 
            <h1> BedBugZ </h1>
            <h2> bug bites to love bites </h2>
        </div>
        <div>
            <ButtonElement 
                icon="favorite"
                text="find a match"
            />
            <ButtonElement 
                icon="park"
                text="view date spots"
            />
            <ButtonElement 
                icon="pest_control"
                text="scan a suitor"
            />
        </div>
        <div>
            33% done
            TODO: Percent Element here
        </div>
    </div>
</template>

<script>
import ButtonElement from '~/components/button.vue';

export default {
    components: {
        ButtonElement
    }
}
</script>