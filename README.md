# Kube-Door

## What is Kube-Door?

Kube-door is a simple reserve proxy for Kubernetes services using HAProxy. It simply watches for services annotates
with `kube-door/ports` and then generate appropriate HAproxy configuration.

The idea is similar to [Marathon-lb](https://github.com/mesosphere/marathon-lb) from Mesos.

## How to use this?

First you need to build the docker image

```
docker build . -t kube-door
```

Then run the docker image under net host. Additionally, you can mount the kubeconfig and relevant certs to kube-door
so it can talk to Kubernetes.

```
docker run -d \
  -v ~/.kube:/kubeconfig \
  -e KUBECONFIG=/kubeconfig/config \
  --name=kube-door
```

You will need to expose your service with annotations. You can annotate your service with `kube-door/ports` with the 
port you want to expose to Kube-door. For example, below is a command to expose port 80 from `your_service`.

```
kubectl annotate svc/your_service kube-door/ports=80
```

In future, proxy by domain can also be supported.

## Why don't you use Ingress or expose your service with LoadBalancer?

If your kuberentes cluster has cloud configuration, then it's best to just use service type `LoadBalancer`. In my case,
the cluster is not configured with cloud so we usually setup the LoadBalancer manually, which takes a lof of work.

[Ingress](https://kubernetes.io/docs/user-guide/ingress/) is still in beta at the time i write this. And it requires
to deploy an Ingress controller plus ingress resource configuration, which will will add more overhead so I prefer
a quick and simple solution for now. This will be easier and faster to use Kube-door and get something running.

In fact, this is very similar to [Service LoadBalancer](https://github.com/kubernetes/contrib/tree/master/service-loadbalancer),
but this requires you to run the load balancer on kubernetes nodes. Having the security requirements cleanly separated
for internal access and external access is more preferred.
