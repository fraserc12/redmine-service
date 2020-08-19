<template>
  <div class="entries-table">
    <h3>Hour Summary</h3>
    <vue-good-table
      :columns="columns"
      :rows="entries"
      :pagination-options="{
          enabled: true,
          mode: 'records',
          perPage: 5
        }"
      :sort-options="{
          enabled: false,
        }"
    />
  </div>
</template>

<script>
export default {
  name: "EntriesTable",
  props: ["entries"],
  data() {
    return {
      columns: [
        {
          label: "Date",
          field: "date",
          type: "date",
          dateInputFormat: "yyyy-MM-dd",
          dateOutputFormat: "iiii PP",
          width: "25%",
        },
        {
          label: "Hours",
          field: "hours",
          type: "number",
          width: "5%",
        },
        {
          label: "Vacation",
          field: "isHoliday",
          width: "5%",
        },
      ],
      noTimeEntries: false,
    };
  },
};
</script>
<style scoped>
.entries-table {
  margin-top: 8%;
}
</style>
