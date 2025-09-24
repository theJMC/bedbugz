<template>
    <div class="smashOrSquash main-background">
        <h1 class="font-white font-32 font-semibold"> BedBugZ </h1>
        <ProfileComponent />
        <div class="footer">
            <button class="smash">🪰 smash</button>
            <button class="squash">❤️ squash</button>
        </div>
    </div>
</template>

<script>
import ProfileComponent from '../components/profile.vue';

export default {
    name: 'SmashOrSquashPage',
    components: {
        ProfileComponent
    }
}
</script>

<style lang="scss">
@import '../main.scss';
.smashOrSquash {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    height: 100vh;
    padding: 24px;
    box-sizing: border-box;
    position: relative;

    h1 {
        margin-bottom: 12px;
        align-self: flex-start;
    }

    .footer {
        width: 100%;
        display: flex;
        justify-content: space-between;
        gap: 12px;

        button {
            flex: 1;
            padding: 12px 0;
            font-size: 1.5rem;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;

            &.smash {
                background-color: #28a745; // Green
                color: white;

                &:hover {
                    background-color: #218838; // Darker green
                }
            }

            &.squash {
                background-color: #dc3545; // Red
                color: white;

                &:hover {
                    background-color: #c82333; // Darker red
                }
            }
        }
    }
}
</style>