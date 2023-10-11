webix.ui({
  type: "space",
  id: "a1",
  rows: [
    {
      view: "toolbar",
      padding: 3,
      elements: [
        {
          view: "button",
          type: "icon",
          icon: "mdi mdi-menu",
          width: 48,
          align: "center",
          click: function () {
            $$("$sidebar1").toggle();
          },
        },
        { view: "label", label: "WAR-teg" },
        {},
        // { view: "button", type: "icon", width: 45, css: "app_button", icon: "mdi mdi-comment",  badge:4},
        // { view: "button", type: "icon", width: 45, css: "app_button", icon: "mdi mdi-bell",  badge:10}
      ],
    },
    {
      cols: [
        {
          view: "sidebar",
          data: menu_data_multi,
          on: {
            onAfterSelect: function (id) {
              webix.message("Selected: " + this.getItem(id).value);
            },
          },
        },
        {
          cols: [
            {
              view: "datatable",
              id: "mylist",
              select: true,
              columns: [
                { id: "name", editor: "text", header: "Nama", adjust: true },
                {
                  id: "desc",
                  editor: "text",
                  header: "Deskripsi",
                  adjust: true,
                },
                { id: "addr", editor: "text", header: "Alamat", adjust: true },
                { id: "dist", editor: "text", header: "Jarak", adjust: true },
              ],
              data: list,
            },
            {
              view: "form",
              maxWidth: 600,
              id: "myform",
              elements: [
                { view: "label", label: "Tambah Warteg", align: "center" },
                { view: "text", name: "name", label: "Nama" },
                { view: "text", name: "addr", label: "Alamat" },
                { view: "text", name: "dist", label: "Jarak" },
                { view: "textarea", name: "desc", label: "Deskripsi" },
                {
                  cols: [
                    {
                      view: "toolbar",
                      id: "mybar",
                      elements: [
                        {
                          view: "button",
                          type: "icon",
                          icon: "wxi-pencil",
                          value: "Save",
                          label: "Save",
                          click: save_data,
                        },
                        {
                          view: "button",
                          type: "icon",
                          icon: "wxi-sync",
                          value: "Reset",
                          label: "Reset",
                          click: () => $$("myform").clear(),
                        },
                        {
                          view: "button",
                          type: "icon",
                          icon: "wxi-trash",
                          value: "Delete",
                          label: "Delete",
                          click: delete_data,
                        },
                      ],
                    },
                  ],
                },
              ],
            },
          ],
        },
      ],
    },
  ],
});

function save_data() {
  const values = $$("myform").getValues();
  if (values.id) $$("mylist").updateItem(values.id, values);
  else {
    webix
      .ajax()
      .headers({
        "Content-Type": "application/json",
      })
      .post(BASE_URL + WARTEG_API, {
        name: values.name,
        desc: values.desc,
        addr: values.addr,
        dist: values.dist,
      })
      .then(
        function (data) {
          const response = data.json();
          console.log(response);
          $$("mylist").add(response.data);
          $$("myform").clear();
        },
        function (err) {
          console.log(err);
        }
      );
  }
}

function delete_data() {
  const id = $$("mylist").getSelectedId();
  if (!id) return;

  webix.confirm({
    title: "Delete",
    text: "Are you sure you want to delete the selected item?",
    callback: function (result) {
      if (result) {
        $$("mylist").remove(id);
        webix
          .ajax()
          .headers({
            "Content-Type": "application/json",
          })
          .del(BASE_URL + WARTEG_API, { id: id.id })
          .then(function (data) {
            const response = data.json();
            console.log(response);
          });
      }
    },
  });
}
