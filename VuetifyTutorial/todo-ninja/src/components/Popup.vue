<template>
    <v-dialog max-width="600px">
        <template v-slot:activator="{on}">

        <v-btn  v-on="on" text slot="activator" class="success">Add new project</v-btn>
        </template>
        <v-card>
            <v-card-title>
                <h2>Add a New Project</h2>
            </v-card-title>
        </v-card>
    </v-dialog>
</template>

<script>
export default {
    
}
</script>