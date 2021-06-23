from apptopo import AppTopo

class CustomAppTopo(AppTopo):

    def __init__(self, *args, **kwargs):
        # Initialize the top topo
        AppTopo.__init__(self, *args, **kwargs)

        manifest, target = kwargs['manifest'], kwargs['target']

        print "Using target:", manifest['targets'][target]
        
        # Add hosts and switches
        #TODO same as in hometopo, but now Host1 is in foregin network
        Host1 = self.addHost( 'h1', ip=#TODO, mac='00:00:00:00:00:01' )
        Host2 = self.addHost( 'h2', ip=#TODO, mac='00:00:00:00:00:02' )
        Host3 = self.addHost( 'h3', ip=#TODO, mac='00:00:00:00:00:03' )
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')