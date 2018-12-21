
Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # Claves ssh para conectarse a la máquina.
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    # Estas varibles tenemos que exportarlas, son las variables que se encargan de identificar la cuenta de azure
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    #Variables para modificar la información de la máquina virtual.
    azure.vm_name = "planificador-diario-iv1819"
    azure.vm_size = "Basic_A2"
    azure.tcp_endpoints = "80"
    azure.location = "westeurope"
    azure.admin_username = "jomaenfe"

  end

  # Aquí es donde aprovisionamos la máquina cuando la creamos
  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end