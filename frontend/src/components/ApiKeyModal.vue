<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <h2 class="form-title">Redmine Details</h2>
            </slot>
          </div>
          <div class="modal-body">
            <slot name="body">
              <FormulateForm v-model="formValues" @submit="hide" class="api-key-form center">
                <FormulateInput
                  type="text"
                  label="API Key:"
                  validation="bail|required|max:40|min:40"
                  name="api_key_form"
                  v-model="api_key"
                  help="Find on your account in Redmine"
                  :validation-messages="{
                            matches: 'Find on your account in Redmine.'
                    }"
                />
                <FormulateInput type="submit" label="Save" class="actions" />
              </FormulateForm>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "ApiKeyModal",
  props: {
    getProjects: { type: Function },
    closeModal: { type: Function },
  },
  data() {
    return {
      formValues: {
        //do something better here?
        api_key_form: this.api_key,
      },
      api_key: localStorage.api_key ? localStorage.api_key : "",
    };
  },
  methods: {
    hide() {
      let oldKey = localStorage.api_key;
      if (oldKey !== this.api_key) {
        localStorage.api_key = this.api_key;
        this.getProjects();
      }
      this.closeModal();
    },
  },
  mount() {
    this.show();
  },
};
</script>
<style scoped>
.center {
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-top: 10%;
  margin-right: 5%;
  margin-left: 5%;
}
button {
  align-items: flex-start;
  background-color: hsla(0, 0%, 0%, 0.01);
  color: hsl(215, 16%, 50%);
  flex-basis: 100%;
  font-size: 12px;
  gap: normal;
  letter-spacing: 1px;
  text-align: center;
}
.actions {
  display: flex;
  margin-bottom: 1em;
}
.actions .formulate-input {
  margin-right: 1em;
  margin-bottom: 0;
}
.form-title {
  margin-top: 0;
  margin-bottom: 3%;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 475px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
