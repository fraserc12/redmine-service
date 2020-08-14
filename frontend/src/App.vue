<template>
  <div id="app">
    <div class="center">
      <h3>Select Project: </h3>
      <v-select :options="projects" 
                label="name" 
                :disabled="!(projects.length)"
                :reduce="project => project.id"
                v-model="selected"
                @input="getTimeEntries"></v-select>

      <br/>
      <div v-if="timeEntries.length > 0">
        <h3>Summary </h3>
        <vue-good-table
          :columns="columns"
          :rows="timeEntries"
          :pagination-options="{
            enabled: true,
            mode: 'records',
            perPage: 5
        }"/>
      </div>
    </div>
  </div>
</template>

<script>export default {
  name: "App",
  data() {
    return {
      projects: [],
      selected: '',
      timeEntries: [],
      columns: [
        {
          label: 'Date',
          field: 'date',
          type: 'date',
          dateInputFormat: 'yyyy-MM-dd',
          dateOutputFormat: 'EEE-PPP',
        },
        {
          label: 'Hours',
          field: 'hours',
          type: 'number',
        },
        {
          label: 'Vacation/PTO/Holiday',
          field: 'isHoliday',
        },
      ],
    }
  },
  beforeMount(){
    this.getProjects();
  },
  methods: {
    async getProjects(){
      const res = await fetch('http://localhost:5000/projects');
      const data = await res.json();
      this.projects = data;
    },
    async getTimeEntries() {
     this.timeEntries = []
     let url = 'http://localhost:5000/time-logged?project_id='+this.selected
     const res = await fetch(url);
     const data = await res.json();
     this.timeEntries = data;
     console.log(this.timeEntries.reverse())
  }
  }
};
</script>

<style scoped>
  .center {
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin-top: 10%;
    margin-right: 30%;
    margin-left: 30%;
  }
</style>