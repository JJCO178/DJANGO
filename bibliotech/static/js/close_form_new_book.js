function handleClose() {
    // Ejecutar acciones adicionales antes de cerrar
    console.log("Modal cerrado");
    // Si necesitas cerrar manualmente:
    const modal = document.getElementById('tuModalId');
    const modalInstance = bootstrap.Modal.getInstance(modal);
    modalInstance.hide();
}