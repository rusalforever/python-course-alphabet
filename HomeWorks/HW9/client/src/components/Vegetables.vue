<template>
  <div class="col-md-6">
    <div>
      <div>
        <h1>Vegetables</h1>
        <hr>
        <br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.vegetable-modal>Add Vegetable</button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Color</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(vegetable, index) in vegetables" :key="index">
            <td>{{ vegetable.name }}</td>
            <td>{{ vegetable.color }}</td>
            <td>
              <button
                type="button"
                class="btn btn-warning btn-sm"
                v-b-modal.vegetable-update-modal
                @click="editVegetable(vegetable)">
                Update
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="onDeleteVegetable(vegetable)">
                Delete
              </button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addVegetableModal"
             id="vegetable-modal"
             title="Add a new vegetable"
             hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addVegetableForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-color-group"
                      label="Color:"
                      label-for="form-color-input">
          <b-form-input id="form-color-input"
                        type="text"
                        v-model="addVegetableForm.color"
                        required
                        placeholder="Enter color">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editVegetableModal"
             id="vegetable-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-color-edit-group"
                      label="Color:"
                      label-for="form-color-edit-input">
          <b-form-input id="form-color-edit-input"
                        type="text"
                        v-model="editForm.color"
                        required
                        placeholder="Enter color">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>

</template>

<script>
  import axios from 'axios';
  import Alert from './Alert';

  export default {
    data() {
      return {
        vegetables: [],
        addVegetableForm: {
          name: '',
          color: '',
        },
        editForm: {
          id: '',
          name: '',
          color: '',
        },
        message: '',
        showMessage: false,
      };
    },
    components: {
      alert: Alert,
    },

    methods: {
      getVegetables() {
        const path = 'http://localhost:5000/vegetables';
        axios.get(path)
          .then((res) => {
            this.vegetables = res.data.vegetables;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      editVegetable(vegetable) {
        this.editForm = vegetable;
      },
      onSubmitUpdate(evt) {
        evt.preventDefault();
        this.$refs.editVegetableModal.hide();
        const payload = {
          name: this.editForm.name,
          color: this.editForm.color,
        };
        this.updateVegetable(payload, this.editForm.id);
      },
      onResetUpdate(evt) {
        evt.preventDefault();
        this.$refs.editVegetableModal.hide();
        this.initForm();
        this.getVegetables();
      },
      updateVegetable(payload, vegetableID) {
        const path = `http://localhost:5000/vegetables/${vegetableID}`;
        console.log(payload)
        axios.put(path, payload)
          .then(() => {
            this.getVegetables();
            this.message = 'Vegetable updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getVegetables();
          });
      },
      removeVegetable(vegetableID) {
        const path = `http://localhost:5000/vegetables/${vegetableID}`;
        axios.delete(path)
          .then(() => {
            this.getVegetables();
            this.message = 'Vegetable removed!';
            this.showMessage = true;
          })
          .catch((error) => {
            this.message = error;
            this.showMessage = true;
            this.getVegetables();
          });
      },
      onDeleteVegetable(vegetable) {
        this.removeVegetable(vegetable.id);
      },
      addVegetable(payload) {
        const path = 'http://localhost:5000/vegetables';
        axios.post(path, payload)
          .then(() => {
            this.getVegetables();
            this.message = 'Vegetable added!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.log(error);
            this.getVegetables();
          });
      },
      initForm() {
        this.addVegetableForm.name = '';
        this.addVegetableForm.color = '';
        this.editForm.name = '';
        this.editForm.color = '';
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addVegetableModal.hide();
        const payload = {
          name: this.addVegetableForm.name,
          color: this.addVegetableForm.color,
        };
        this.addVegetable(payload);
        this.initForm();
      },
      onReset(evt) {
        evt.preventDefault();
        this.$refs.addVegetableModal.hide();
        this.initForm();
      },
    },
    created() {
      this.getVegetables();
    },
  };
</script>
