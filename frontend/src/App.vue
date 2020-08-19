<template>
  <div id="app">
    <FormulateInput class="topright" type="button" label="Redmine Key" @click="openModal" />
    <ApiKeyModal v-if="showModal" ref="modal" :getProjects="getProjects" :closeModal="closeModal" />
    <div class="center">
      <h3>Select Project:</h3>
      <v-select
        :options="projects"
        label="name"
        :disabled="!(projects.length)"
        :reduce="project => project.id"
        v-model="projectId"
        @input="getTimeEntries">
      </v-select>

      <div v-if="timeEntries && timeEntries.length > 0">
        <EntriesTable :entries="timeEntries" />
      </div>
      <div v-if="loading">
        <loading :active.sync="loading" :is-full-page="true"></loading>
      </div>
      <div v-if="timeEntries && timeEntries.length <= 0" class="warning">No Time Entries found! :(</div>
      <div v-if="showError" class="error-message">Fetch Error.. please check your API Key is correct!</div>
    </div>
  </div>
</template>

<script>
import ApiKeyModal from "./components/ApiKeyModal";
import EntriesTable from "./components/EntriesTable";

export default {
  name: "App",
  components: {
    ApiKeyModal,
    EntriesTable,
  },
  data() {
    return {
      projects: [],
      projectId: "",
      timeEntries: null,
      showModal: false,
      showError: false,
      loading: false,
    };
  },
  mounted() {
    if (!("api_key" in localStorage)) {
      this.showModal = true;
    } else {
      this.getProjects();
    }
  },
  methods: {
    async getProjects() {
      let url =
        "http://localhost:5000/projects?api_key=" + localStorage.api_key;
      this.loading = true;
      fetch(url)
        .then(async (res) => {
          if (!res.ok) {
            const error = (data && data.message) || res.statusText;
            return Promise.reject(error);
          }
          this.loading = false;
          this.showError = false;
          const data = await res.json();
          this.projects = data;
        })
        .catch((error) => {
          this.showError = true;
          this.loading = false;
          console.error("There was an error!", error);
        });
    },
    async getTimeEntries() {
      let url =
        "http://localhost:5000/time-logged?project_id=" +
        this.projectId +
        "&api_key=" +
        localStorage.api_key;
      this.loading = true;
      fetch(url)
        .then(async (res) => {
          if (!res.ok) {
            const error = (data && data.message) || res.statusText;
            return Promise.reject(error);
          }
          this.loading = false;
          this.showError = false;
          const data = await res.json();
          this.timeEntries = data.reverse();
          this.entriesFound = this.timeEntries.length > 0 ? false : true;
        })
        .catch((error) => {
          this.showError = true;
          this.loading = false;
          console.error("There was an error!", error);
        });
    },
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
  },
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
.topright {
  position: absolute;
  top: 10px;
  right: 10px;
}
.warning {
  margin-top: 8%;
}
.error-message {
  background-color: #fce4e4;
  border: 1px solid #fcc2c3;
  float: left;
  padding: 20px 30px;
  margin-top: 5%;
}
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");
#app {
  font-family: "Montserrat", sans-serif;
}
</style>