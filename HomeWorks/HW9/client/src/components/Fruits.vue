<template>
  <div class="col-md-6">
    <div>
      <div>
        <h1>Fruits</h1>
        <hr>
        <br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.fruit-modal>Add Fruit</button>
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
          <tr v-for="(fruit, index) in fruits" :key="index">
            <td>{{ fruit.name }}</td>
            <td>{{ fruit.color }}</td>
            <td>
              <button
                type="button"
                class="btn btn-warning btn-sm"
                v-b-modal.fruit-update-modal
                @click="editFruit(fruit)">
                Update
              </button>
              <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="onDeleteFruit(fruit)">
                Delete
              </button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addFruitModal"
             id="fruit-modal"
             title="Add a new fruit"
             hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addFruitForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-color-group"
                      label="Color:"
                      label-for="form-color-input">
          <b-form-input id="form-color-input"
                        type="text"
                        v-model="addFruitForm.color"
                        required
                        placeholder="Enter color">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editFruitModal"
             id="fruit-update-modal"
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
        fruits: [],
        addFruitForm: {
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
      getFruits() {
        const path = 'http://localhost:5000/fruits';
        axios.get(path)
          .then((res) => {
            this.fruits = res.data.fruits;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      editFruit(fruit) {
        this.editForm = fruit;
      },
      onSubmitUpdate(evt) {
        evt.preventDefault();
        this.$refs.editFruitModal.hide();
        const payload = {
          name: this.editForm.name,
          color: this.editForm.color,
        };
        this.updateFruit(payload, this.editForm.id);
      },
      onResetUpdate(evt) {
        evt.preventDefault();
        this.$refs.editFruitModal.hide();
        this.initForm();
        this.getFruits();
      },
      updateFruit(payload, fruitID) {
        const path = `http://localhost:5000/fruits/${fruitID}`;
        console.log(payload)
        axios.put(path, payload)
          .then(() => {
            this.getFruits();
            this.message = 'Fruit updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getFruits();
          });
      },
      removeFruit(fruitID) {
        const path = `http://localhost:5000/fruits/${fruitID}`;
        axios.delete(path)
          .then(() => {
            this.getFruits();
            this.message = 'Fruit removed!';
            this.showMessage = true;
          })
          .catch((error) => {
            this.message = error;
            this.showMessage = true;
            this.getFruits();
          });
      },
      onDeleteFruit(fruit) {
        this.removeFruit(fruit.id);
      },
      addFruit(payload) {
        const path = 'http://localhost:5000/fruits';
        axios.post(path, payload)
          .then(() => {
            this.getFruits();
            this.message = 'Fruit added!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.log(error);
            this.getFruits();
          });
      },
      initForm() {
        this.addFruitForm.name = '';
        this.addFruitForm.color = '';
        this.editForm.name = '';
        this.editForm.color = '';
      },
      onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addFruitModal.hide();
        const payload = {
          name: this.addFruitForm.name,
          color: this.addFruitForm.color,
        };
        this.addFruit(payload);
        this.initForm();
      },
      onReset(evt) {
        evt.preventDefault();
        this.$refs.addFruitModal.hide();
        this.initForm();
      },
    },
    created() {
      this.getFruits();
    },
  };
</script>
