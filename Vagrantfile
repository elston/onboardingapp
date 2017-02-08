VAGRANTFILE_API_VERSION = "2"
#.....
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    #.....
    config.vm.box = "ubuntu/trusty64"
    # ..
    config.vm.network :forwarded_port, host: 8005, guest: 8000    
    # ..
    config.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
    # ..
    config.vm.provision :shell, :path => "vg_bootstrap.sh"    
end
