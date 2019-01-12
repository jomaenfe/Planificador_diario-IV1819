# Usamos la versión 2 del plugin azure-vagrant.
Vagrant.configure('2') do |configuracion| # Variable de configuración para modificar la configuración de la "box" y claves que vamos a usar.
  configuracion.vm.box = 'azure-vagrant-box' # Usamos como base para el funcionamiento de vagrant la "box" que hemos añadido a la configuración anteriormente.

  # Claves ssh para conectarse a la máquina.
  configuracion.ssh.private_key_path = '~/.ssh/id_rsa' # Cogemos la clave ssh almacenada en esta ruta de nuestro sistema para conectarnos a la máquina
                                                       # sin necesidad de contraseña.
  

  # Variable de contexto o topicalizador.
  
  configuracion.vm.provider :azure do |planificador_diario, override| # Creo la variable planificador_diario a partir del topicalizador de azure para 
                                                                      # poder darle información al proveedor tanto de variables para la conexión a 
                                                                      # nuestra cuenta como de parámetros para la creación de nuestra máquina virtual. 

    # Estas varibles tenemos que exportarlas, son las variables que se encargan de identificar la cuenta de azure
    planificador_diario.tenant_id = ENV['id_tenant']
    planificador_diario.client_id = ENV['id_cliente']
    planificador_diario.client_secret = ENV['passw_cliente']
    planificador_diario.subscription_id = ENV['id_subscripcion']

    #Variables para modificar la información de la máquina virtual.
    planificador_diario.vm_name = "planificador-diario-1819" # Con esto modifico el nombre de nuestra máquina virtual.
    planificador_diario.vm_size = "Basic_A2" # Este es el identificador del hardware que va a usar la máquina. 
    planificador_diario.tcp_endpoints = "80" # Abro el puerto 80 en la máquina.
    planificador_diario.location = "westeurope" # Defino el lugar donde estará ubicada la máquina.
    planificador_diario.admin_username = "jomaenfe" # Defino el nombre de usuario del adminsitrador de la máquina virtual.

  end

  # Aquí es donde aprovisionamos la máquina cuando la creamos
  configuracion.vm.provision :ansible do |provisionamiento| # Creo la variable "provisionamiento" a partir del topicalizador de ansible, con la que 
                                                            # haremos la provisión de nuestra máquina una vez creada y funcionando.
  
     provisionamiento.playbook = "provision/playbook.yml" # Provisiono la máquina virtual.
  end

end